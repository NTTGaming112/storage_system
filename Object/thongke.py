import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from db import create_connection, close_connection
from PyQt6.QtCore import QDateTime

class AddEditDialog(QDialog):
    def __init__(self, title, fields, values=None):
        super().__init__()
        self.setWindowTitle(title)
        self.layout = QVBoxLayout()
        
        self.field_widgets = {}
        for field in fields:
            label = QLabel(field)
            line_edit = QLineEdit()
            if values and field in values:
                line_edit.setText(values[field])
            self.layout.addWidget(label)
            self.layout.addWidget(line_edit)
            self.field_widgets[field] = line_edit
        
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.accept)
        self.layout.addWidget(self.save_button)
        
        self.setLayout(self.layout)

    def get_values(self):
        return {field: widget.text() for field, widget in self.field_widgets.items()}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        
        self.loadButton.clicked.connect(self.load_table)
        self.addButton.clicked.connect(self.add_record)
        self.editButton.clicked.connect(self.edit_record)
        self.deleteButton.clicked.connect(self.delete_record)
        self.generateReportButton.clicked.connect(self.generate_report)  # Connect the report button

        # Load available tables in the comboBox
        self.tableComboBox.addItems(["category", "product", "user", "order", "order_item"])
        self.periodComboBox.addItems(["Daily", "Monthly", "Yearly"])  # Add period options for the report

    def load_table(self):
        table_name = self.tableComboBox.currentText()
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        headers = [i[0] for i in cursor.description]
        close_connection(connection)
        
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)
        
        for row_index, row in enumerate(rows):
            for col_index, item in enumerate(row):
                self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(item)))

    def add_record(self):
        table_name = self.tableComboBox.currentText()
        fields = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
        
        dialog = AddEditDialog("Add Record", fields)
        if dialog.exec():
            values = dialog.get_values()
            placeholders = ", ".join(["%s"] * len(values))
            columns = ", ".join(values.keys())
            
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", tuple(values.values()))
            connection.commit()
            close_connection(connection)
            
            self.load_table()

    def edit_record(self):
        table_name = self.tableComboBox.currentText()
        selected_items = self.tableWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "No Selection", "Please select a record to edit.")
            return
        
        row = selected_items[0].row()
        fields = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
        values = {field: self.tableWidget.item(row, i).text() for i, field in enumerate(fields)}
        
        dialog = AddEditDialog("Edit Record", fields, values)
        if dialog.exec():
            new_values = dialog.get_values()
            set_clause = ", ".join([f"{k} = %s" for k in new_values.keys()])
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(f"UPDATE {table_name} SET {set_clause} WHERE id = %s", tuple(new_values.values()) + (values['id'],))
            connection.commit()
            close_connection(connection)
            
            self.load_table()

    def delete_record(self):
        table_name = self.tableComboBox.currentText()
        selected_items = self.tableWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "No Selection", "Please select a record to delete.")
            return
        
        row = selected_items[0].row()
        record_id = self.tableWidget.item(row, 0).text()
        
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE id = %s", (record_id,))
        connection.commit()
        close_connection(connection)
        
        self.load_table()

    def generate_report(self):
        period = self.periodComboBox.currentText()
        query = ""
        
        if period == "Daily":
            query = """
                SELECT DATE(date) AS period, SUM(total_price) AS revenue
                FROM `order`
                GROUP BY DATE(date)
                ORDER BY DATE(date);
            """
        elif period == "Monthly":
            query = """
                SELECT DATE_FORMAT(date, '%Y-%m') AS period, SUM(total_price) AS revenue
                FROM `order`
                GROUP BY DATE_FORMAT(date, '%Y-%m')
                ORDER BY DATE_FORMAT(date, '%Y-%m');
            """
        elif period == "Yearly":
            query = """
                SELECT YEAR(date) AS period, SUM(total_price) AS revenue
                FROM `order`
                GROUP BY YEAR(date)
                ORDER BY YEAR(date);
            """
        
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = [i[0] for i in cursor.description]
        close_connection(connection)
        
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)
        
        for row_index, row in enumerate(rows):
            for col_index, item in enumerate(row):
                self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(item)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
