from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from datetime import datetime

from ui_main_view import Ui_MainWindow
from db import *
from user import *
from category import *
from product import *
from order import *
from order_item import *

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
        self.setWindowTitle("Menu")

        self.user_changes = {}
        self.product_changes = {}
        self.order_changes = {}

        self.table_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_order.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_product.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_thongke.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.edit_mode_button.setCheckable(True)
        self.edit_mode_button.setChecked(False)
        self.edit_mode_button.toggled.connect(self.toggle_edit_mode)

        self.icon_name_widget.setHidden(True)
        self.stackedWidget.setCurrentIndex(0)
        self.edit_user.setEnabled(False)

        self.user_1.clicked.connect(self.switch_to_userPage)
        self.user_2.clicked.connect(self.switch_to_userPage)

        self.product_1.clicked.connect(self.switch_to_productPage)
        self.product_2.clicked.connect(self.switch_to_productPage)

        self.order_1.clicked.connect(self.switch_to_orderPage)
        self.order_2.clicked.connect(self.switch_to_orderPage)

        self.thongke_1.clicked.connect(self.switch_to_thongkePage)
        self.thongke_2.clicked.connect(self.switch_to_thongkePage)

        self.load_user_data()
        self.add_user.clicked.connect(self.add_user_data)    
        self.table_user.cellChanged.connect(self.update_user_data)
        self.edit_user.clicked.connect(self.save_user_changes)     
        self.delete_user.clicked.connect(self.delete_selected_users)

        self.load_category()
        self.load_product.clicked.connect(self.load_product_data)
        self.add_product.clicked.connect(self.add_product_data)    
        self.table_product.cellChanged.connect(self.update_product_data)
        self.edit_product.clicked.connect(self.save_product_changes)     
        self.delete_product.clicked.connect(self.delete_selected_products)

        self.load_username()
        self.load_order.clicked.connect(self.load_order_data)  
        self.add_order.clicked.connect(self.add_order_data)    
        self.delete_order.clicked.connect(self.delete_selected_orders)
  
        self.load_thongke.clicked.connect(self.get_all_dates)

        
        

    def switch_to_userPage(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_productPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_orderPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_thongkePage(self):
        self.stackedWidget.setCurrentIndex(3)
    
    def toggle_edit_mode(self, checked):
        if checked:
            self.table_user.setEditTriggers(QAbstractItemView.DoubleClicked)
            self.table_order.setEditTriggers(QAbstractItemView.DoubleClicked)
            self.table_product.setEditTriggers(QAbstractItemView.DoubleClicked)
            self.table_thongke.setEditTriggers(QAbstractItemView.DoubleClicked)
            self.edit_mode_button.setText("Tắt chế độ chỉnh sửa")
        else:
            self.table_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.table_order.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.table_product.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.table_thongke.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.edit_mode_button.setText("Bật chế độ chỉnh sửa")          

        for row in range(self.table_user.rowCount()):
            item = self.table_user.item(row, 0)
            if item:
                item.setFlags(item.flags() & ~ Qt.ItemIsEditable)

        for row in range(self.table_product.rowCount()):
            item = self.table_product.item(row, 0)
            if item:
                item.setFlags(item.flags() & ~ Qt.ItemIsEditable)

        for row in range(self.table_order.rowCount()):
            item = self.table_order.item(row, 0)
            if item:
                item.setFlags(item.flags() & ~ Qt.ItemIsEditable)

        for row in range(self.table_thongke.rowCount()):
            item = self.table_thongke.item(row, 0)
            if item:
                item.setFlags(item.flags() & ~ Qt.ItemIsEditable)



    def load_user_data(self):
        users = User.fetch()
        self.table_user.setRowCount(len(users))
        self.table_user.setColumnCount(len(users[0])+1)
        for row_idx, user in enumerate(users):            
            for col_idx, data in enumerate(user):
                self.table_user.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))
            checkbox_widget = QCheckBox()
            checkbox_widget.setStyleSheet("QCheckBox::indicator { width: 20px; height: 20px;}")
            self.table_user.setCellWidget(row_idx, len(user), checkbox_widget)
          
    def add_user_data(self):
        dialog = QDialog()
        dialog.setWindowTitle("Add User")

        form_layout = QFormLayout()
        username_input = QLineEdit()
        password_input = QLineEdit()
        address_input = QLineEdit()
        phone_input = QLineEdit()
        email_input = QLineEdit()

        form_layout.addRow("Tên:", username_input)
        form_layout.addRow("Mật khẩu:", password_input)
        form_layout.addRow("Địa chỉ:", address_input)
        form_layout.addRow("SĐT:", phone_input)
        form_layout.addRow("Email:", email_input)

        error_label = QLabel("")
        error_label.setStyleSheet("color: red")
        form_layout.addRow(error_label)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(buttons)
        dialog.setLayout(layout)

        while True:
            if dialog.exec() == QDialog.Accepted:
                user_data = {
                    "username": username_input.text(),
                    "password": password_input.text(),
                    "address": address_input.text(),
                    "phone": phone_input.text(),
                    "email": email_input.text()
                }
                if any(not value for value in user_data.values()):
                    error_label.setText("Nhập đủ thông tin cần thiết.")
                    continue

                if not User.add(user_data):
                    error_label.setText("Tên đã tồn tại, vui lòng nhập tên khác.")
                else:
                    break
            else:
                break
        self.load_user_data()
        self.load_username()
        self.user_changes.clear()
        self.edit_user.setEnabled(False)

    def update_user_data(self, row, column):
        id_item = self.table_user.item(row, 0)
        if id_item is None:
            return

        user_id = id_item.text()
        new_value = self.table_user.item(row, column).text()

        columns = ["id", "username", "password", "address", "phone", "email", "checkbox"]
        column_name = columns[column]

        if column_name == "id" or column_name == "check_box":
            return  

        if user_id not in self.user_changes:
            self.user_changes[user_id] = {}
        self.user_changes[user_id][column_name] = new_value

        self.edit_user.setEnabled(True)

    def save_user_changes(self):
        success = True
        for user_id, updates in self.user_changes.items():
            for column, value in updates.items():
                if not User.update(user_id, column, value):
                    success = False
                    break
            if not success:
                break

        if success:
            QMessageBox.information(self, "Success", "Cập nhật hoàn tất")           
        else:
            QMessageBox.warning(self, "Error", "Tên đã tồn tại")

        self.load_user_data()
        self.edit_user.setEnabled(False)
        self.user_changes.clear()
        self.add_user.setEnabled(True)

    def delete_selected_users(self):
        rows_to_delete = []
        ids_to_delete = []

        for row in range(self.table_user.rowCount()):
            checkbox_widget = self.table_user.cellWidget(row, 6)
            if checkbox_widget is not None and checkbox_widget.isChecked():
                rows_to_delete.append(row)
                item = self.table_user.item(row, 0)
                if item:
                    ids_to_delete.append(int(item.text()))

        if not rows_to_delete:
            QMessageBox.warning(self, "Error", "Không có người dùng nào được chọn")
            return

        success = True
        for user_id in ids_to_delete:
            if not User.delete(user_id):
                success = False
                break

        if success:
            QMessageBox.information(self, "Error", f"Đẫ xóa {len(ids_to_delete)} người dùng")
            
        else:
            QMessageBox.warning(self, "Error", "Không thể xóa")

        for row in reversed(rows_to_delete):
            self.table_user.removeRow(row)

        self.edit_user.setEnabled(False)
        self.user_changes.clear()



    def load_category(self):
        categories = Category.fetch()
        for category in categories:
            self.comboBox_product.addItem(category[0])

    def load_product_data(self):
        caterogy_id = self.comboBox_product.currentText()
        products = Product.fetch(caterogy_id)
        self.table_product.setRowCount(len(products))
        self.table_product.setColumnCount(len(products[0])+1)
        for row_idx, product in enumerate(products):            
            for col_idx, data in enumerate(product):
                self.table_product.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))
            checkbox_widget = QCheckBox()
            checkbox_widget.setStyleSheet("QCheckBox::indicator { width: 20px; height: 20px;}")
            self.table_product.setCellWidget(row_idx, len(product), checkbox_widget)

        self.edit_product.setEnabled(False)
        self.product_changes.clear()
        self.add_product.setEnabled(True)

    def add_product_data(self):
        dialog = QDialog()
        dialog.setWindowTitle("Add Product")

        form_layout = QFormLayout()
        name_input = QLineEdit()
        price_input = QLineEdit()
        quantity_input = QLineEdit()

        form_layout.addRow("Tên sản phẩm:", name_input)
        form_layout.addRow("Giá:", price_input)
        form_layout.addRow("Tồn kho:", quantity_input)

        error_label = QLabel("")
        error_label.setStyleSheet("color: red")
        form_layout.addRow(error_label)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(buttons)
        dialog.setLayout(layout)

        while True:
            if dialog.exec() == QDialog.Accepted:
                product_data = {
                    "name": name_input.text(),
                    "price": price_input.text(),
                    "quantity": quantity_input.text()
                }
                if any(not value for value in product_data.values()):
                    error_label.setText("Nhập đủ thông tin cần thiết.")
                    continue

                if not Product.add(product_data,self.comboBox_product.currentText()):
                    error_label.setText("Tên sản phẩm đã tồn tại, vui lòng nhập tên khác.")
                else:
                    break
            else:
                break

        self.load_product_data()
        self.product_changes.clear()
        self.edit_product.setEnabled(False)

    def update_product_data(self, row, column):
        id_product = self.table_product.item(row, 0)
        if id_product is None:
            return

        product_id = id_product.text()
        new_value = self.table_product.item(row, column).text()

        columns = ["id", "name", "price", "quantity", "checkbox"]
        column_name = columns[column]

        if column_name == "id" or column_name == "check_box":
            return  

        if product_id not in self.product_changes:
            self.product_changes[product_id] = {}
        self.product_changes[product_id][column_name] = new_value

        self.edit_product.setEnabled(True)
        
    def save_product_changes(self):
        success = True
        for product_id, updates in self.product_changes.items():
            for column, value in updates.items():
                if not Product.update(product_id, column, value, self.comboBox_product.currentText()):
                    success = False
                    break
            if not success:
                break

        if success:
            QMessageBox.information(self, "Success", "Cập nhật hoàn tất")           
        else:
            QMessageBox.warning(self, "Error", "Tên sản phẩm đã tồn tại")

        self.load_product_data()
        self.edit_product.setEnabled(False)
        self.product_changes.clear()
        self.add_product.setEnabled(True)

    def delete_selected_products(self):
        rows_to_delete = []
        ids_to_delete = []

        for row in range(self.table_product.rowCount()):
            checkbox_widget = self.table_product.cellWidget(row, 4)
            if checkbox_widget is not None and checkbox_widget.isChecked():
                rows_to_delete.append(row)
                item = self.table_product.item(row, 0)
                if item:
                    ids_to_delete.append(int(item.text()))

        if not rows_to_delete:
            QMessageBox.warning(self, "Error", "Không có sản phẩm nào được chọn")
            return

        success = True
        for product_id in ids_to_delete:
            if not Product.delete(product_id,self.comboBox_product.currentText()):
                success = False
                break

        if success:
            QMessageBox.information(self, "Error", f"Đẫ xóa {len(ids_to_delete)} sản phẩm")
            
        else:
            QMessageBox.warning(self, "Error", "Không thể xóa")

        for row in reversed(rows_to_delete):
            self.table_product.removeRow(row)

        self.edit_product.setEnabled(False)
        self.product_changes.clear()



    def load_username(self):
        connection = create_connection()
        if connection is None:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT username FROM user")
            users = cursor.fetchall()
            self.comboBox_order_nameid.clear()
            for user in users:
                self.comboBox_order_nameid.addItem(user[0])

        except Exception as e:
            print(f"Error loading categories: {e}")
        finally:
            cursor.close()
            connection.close()

    def load_order_data(self):
        name_id = self.comboBox_order_nameid.currentText()
        orders = Order.fetch(name_id)
        if orders == []:
            QMessageBox.information(self, "Success", "Không có đơn hàng nào")
        else:
            self.table_order.setRowCount(len(orders))
            self.table_order.setColumnCount(len(orders[0])+2)
            for row_idx, order in enumerate(orders):            
                for col_idx, data in enumerate(order):
                    self.table_order.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))
                load_data_link = QLabel(self.centralwidget)
                load_data_link.setText(f'<a href="{row_idx}">Chi tiết</a>')
                load_data_link.setAlignment(Qt.AlignmentFlag.AlignCenter)
                load_data_link.setOpenExternalLinks(False)
                load_data_link.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
                load_data_link.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                load_data_link.linkActivated.connect(self.load_order_items_data)
                self.table_order.setCellWidget(row_idx, len(order), load_data_link)

                checkbox_widget = QCheckBox()
                checkbox_widget.setStyleSheet("QCheckBox::indicator { width: 20px; height: 20px;}")
                self.table_order.setCellWidget(row_idx, len(order)+1, checkbox_widget)

        self.add_order.setEnabled(True)

    def load_order_items_data(self, row_idx):   
        order_id = self.table_order.item(int(row_idx), 0).text()
        order_items = OrderItem.fetch(order_id)
        
        detail_dialog = QDialog()
        detail_dialog.setWindowTitle('Chi Tiết Đơn Hàng')
        detail_dialog.setGeometry(100, 100, 600, 400)

        table_widget = QTableWidget()
        table_widget.setColumnCount(4)
        table_widget.setHorizontalHeaderLabels(['Tên sản phẩm', 'Giá', 'Số lượng', 'Tổng tiền'])
        table_widget.setRowCount(len(order_items))
        table_widget.setColumnWidth(0, 200) 
        table_widget.setColumnWidth(1, 100) 
        table_widget.setColumnWidth(2, 100)  
        table_widget.setColumnWidth(3, 150)  
        table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(detail_dialog.accept)
        buttons.rejected.connect(detail_dialog.reject)

        for row_idx, item in enumerate(order_items):
            for col_idx, data in enumerate(item):
                table_widget.setItem(row_idx,col_idx, QTableWidgetItem(str(data)))

        layout = QVBoxLayout()
        layout.addWidget(table_widget)
        layout.addWidget(buttons)
        detail_dialog.setLayout(layout)

        while True:
            if detail_dialog.exec() == QDialog.Accepted:
                break
            else:
                break
        
    def add_order_data(self):       
        order_dialog = QDialog()
        order_dialog.setWindowTitle('Tạo Đơn Hàng')
        order_dialog.setGeometry(100, 100, 600, 400)

        comboBox_category = QComboBox()
        categories = Category.fetch()
        for category in categories: 
            comboBox_category.addItem(category[0])
        
        comboBox_product = QComboBox()

        spinBox_quantity = QSpinBox()
        spinBox_quantity.setMinimum(1)

        add_button = QPushButton("Thêm")
        delete_button = QPushButton("Xoá")

        table_add_order = QTableWidget()
        table_add_order.setColumnCount(5)
        table_add_order.setHorizontalHeaderLabels(['Tên sản phẩm', 'Giá', 'Số lượng', 'Tổng tiền', 'Checkbox'])
        table_add_order.setEditTriggers(QAbstractItemView.NoEditTriggers)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        

        layout = QGridLayout()
        layout.addWidget(comboBox_category, 0, 0)
        layout.addWidget(comboBox_product, 0, 1)
        layout.addWidget(spinBox_quantity, 0, 2)
        layout.addWidget(add_button, 0, 3)
        layout.addWidget(delete_button, 0, 4)
        layout.addWidget(table_add_order, 1, 0, 1, 5)
        layout.addWidget(buttons, 2, 0, 1, 5)
        order_dialog.setLayout(layout)

        def update_products():
            comboBox_product.clear()
            products = Product.fetch(comboBox_category.currentText())
            for product in products: 
                comboBox_product.addItem(product[1])

        def update_quantity():
            quantity = Product.fetch_product(comboBox_product.currentText())[2]
            spinBox_quantity.setMaximum(quantity)

        def add_product_to_table():
            product_name = comboBox_product.currentText()
            price = Product.fetch_product(product_name)[1]
            quantity = spinBox_quantity.value()
            total_price = price * quantity
            product_quantity = Product.fetch_product(product_name)[2]
            for row in range(table_add_order.rowCount()):
                item = table_add_order.item(row, 0)
                if item is not None and item.text() == product_name:
                    current_quantity_item = table_add_order.item(row, 2)
                    current_quantity = int(current_quantity_item.text())
                    new_quantity = current_quantity + quantity
                    if new_quantity > product_quantity:
                        QMessageBox.warning(order_dialog, "Warning", "Không đủ số lượng sản phẩm.")
                        return
                    current_quantity_item.setText(str(new_quantity))

                    price_item = table_add_order.item(row, 1)
                    price = float(price_item.text())

                    total_price_item = table_add_order.item(row, 3)
                    new_total = price * new_quantity
                    total_price_item.setText(f"{new_total:.2f}")
                    return
            
            checkbox_widget = QCheckBox()
            checkbox_widget.setStyleSheet("QCheckBox::indicator { width: 20px; height: 20px;}")

            row_position = table_add_order.rowCount()
            table_add_order.insertRow(row_position)
            table_add_order.setItem(row_position, 0, QTableWidgetItem(product_name))
            table_add_order.setItem(row_position, 1, QTableWidgetItem(str(price)))
            table_add_order.setItem(row_position, 2, QTableWidgetItem(str(quantity)))
            table_add_order.setItem(row_position, 3, QTableWidgetItem(str(total_price)))
            table_add_order.setCellWidget(row_position, 4, checkbox_widget)
        
        def delete_product_from_table():    
            rows_to_delete = []

            for row in range(table_add_order.rowCount()):
                checkbox_widget = table_add_order.cellWidget(row, 4)
                if checkbox_widget is not None and checkbox_widget.isChecked():
                    rows_to_delete.append(row)

            if not rows_to_delete:
                QMessageBox.warning(order_dialog, "Error", "Không có sản phẩm nào được chọn")
                return            
                
            for row in reversed(rows_to_delete):
                table_add_order.removeRow(row)

        def save_order_to_db(username, total_price, order_items):                    
            date = datetime.now()
            user_id = User.fetch_id(username)
            order_id = Order.add(date, total_price, user_id)
            for order_item in order_items:  
                OrderItem.add(*order_item,order_id)

        def on_ok_clicked():
            if table_add_order.rowCount() == 0:
                QMessageBox.warning(order_dialog, "Warning", "Cần thêm ít nhất 1 món")
                return           
            
            username = self.comboBox_order_nameid.currentText() 
            total_price = 0.0
            order_items = []
            
            for row in range(table_add_order.rowCount()):
                product_name = table_add_order.item(row, 0).text()
                price = float(table_add_order.item(row, 1).text())
                quantity = int(table_add_order.item(row, 2).text())
                total = float(table_add_order.item(row, 3).text())
                total_price += total
                product_id = Product.fetch_product(product_name)[0]                            
                order_items.append([quantity, product_id])
                Product.update_quantity(product_id, quantity)
            
            save_order_to_db(username, total_price, order_items)
            order_dialog.accept()

        buttons.accepted.connect(on_ok_clicked)
        buttons.rejected.connect(order_dialog.reject)
        comboBox_category.currentTextChanged.connect(update_products)
        comboBox_product.currentTextChanged.connect(update_quantity)
        add_button.clicked.connect(add_product_to_table)
        delete_button.clicked.connect(delete_product_from_table)

        update_products()

        if order_dialog.exec() == QDialog.Accepted:
            print("Order created")
            self.load_order_data()
        else:
            print("Order creation cancelled")

    def delete_selected_orders(self):
        rows_to_delete = []
        ids_to_delete = []

        for row in range(self.table_order.rowCount()):
            checkbox_widget = self.table_order.cellWidget(row, 4)
            if checkbox_widget is not None and checkbox_widget.isChecked():
                rows_to_delete.append(row)
                item = self.table_order.item(row, 0)
                if item:
                    ids_to_delete.append(int(item.text()))

        if not rows_to_delete:
            QMessageBox.warning(self, "Error", "Không có đơn hàng nào được chọn")
            return

        success = True
        for order_id in ids_to_delete:
            if not Order.delete(order_id):
                success = False
                break

        if success:
            QMessageBox.information(self, "Success", f"Đẫ xóa {len(ids_to_delete)} đơn hàng")
            
        else:
            QMessageBox.warning(self, "Error", "Không thể xóa")

        for row in reversed(rows_to_delete):
            self.table_order.removeRow(row)

    def get_all_dates(self):
        time = self.comboBox_thongke.currentIndex()
        connection = create_connection()
        cursor = connection.cursor()

        if time == 0:            
            cursor.execute("SELECT DISTINCT DATE(date) FROM `order`")
            datas = []
            for row in cursor.fetchall():
                date = row[0].strftime('%Y-%m-%d')
                cursor.execute("SELECT SUM(total_price) FROM `order` WHERE DATE(date) = %s", (date,))
                price = cursor.fetchone()[0]
                datas.append([date, price])
            
        elif time == 1:
            cursor.execute("SELECT DISTINCT DATE_FORMAT(date, '%Y-%m') AS month FROM `order`")
            datas = []
            for row in cursor.fetchall():
                month = row[0]
                cursor.execute("SELECT SUM(total_price) FROM `order` WHERE DATE_FORMAT(date, '%Y-%m') = %s", (month,))
                price = cursor.fetchone()[0]
                datas.append([month, price])

        elif time == 2:
            cursor.execute("SELECT DISTINCT DATE_FORMAT(date, '%Y') AS year FROM `order`")
            datas = []
            for row in cursor.fetchall():
                year = row[0]
                cursor.execute("SELECT SUM(total_price) FROM `order` WHERE DATE_FORMAT(date, '%Y') = %s", (year,))
                price = cursor.fetchone()[0]
                datas.append([year, price])

        cursor.close()
        self.table_thongke.setColumnCount(len(datas[0]) + 1)
        self.table_thongke.setRowCount(len(datas))
        self.table_thongke.setHorizontalHeaderLabels(['Thời gian', 'Tổng cộng', 'Chi Tiết'])
        
        for row_idx, date in enumerate(datas):
            for col_idx, data in enumerate(date):
                if col_idx == 1:
                    data = f"{data}$"
                self.table_thongke.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))
            load_data_link = QLabel(self.centralwidget)
            load_data_link.setText(f'<a href="{time},{row_idx}">Chi tiết</a>')
            load_data_link.setAlignment(Qt.AlignmentFlag.AlignCenter)
            load_data_link.setOpenExternalLinks(False)
            load_data_link.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
            load_data_link.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            
            load_data_link.linkActivated.connect(self.load_thongke_data)
            self.table_thongke.setCellWidget(row_idx, len(date), load_data_link)

    def load_thongke_data(self, row):
        time, row_idx = row.strip().split(',')
        date = self.table_thongke.item(int(row_idx), 0).text()
        connection = create_connection()
        cursor = connection.cursor()
        if time == '0':
            query = """
                SELECT 
                    product.name AS ProductName,
                    product.price AS ProductPrice,
                    SUM(order_item.quantity) AS TotalQuantity,
                    SUM(order_item.quantity * product.price) AS TotalRevenue
                FROM 
                    `order`
                JOIN 
                    order_item ON `order`.id = order_item.order_id
                JOIN 
                    product ON order_item.product_id = product.id
                WHERE 
                    DATE(`order`.date) = %s
                GROUP BY 
                    product.id
                ORDER BY 
                    TotalRevenue DESC
            """
            cursor.execute(query, (date,))
            datas = cursor.fetchall()
        elif time == '1':
            query = """
                SELECT 
                    product.name AS ProductName,
                    product.price AS ProductPrice,
                    SUM(order_item.quantity) AS TotalQuantity,
                    SUM(order_item.quantity * product.price) AS TotalRevenue
                FROM 
                    `order`
                JOIN 
                    order_item ON `order`.id = order_item.order_id
                JOIN 
                    product ON order_item.product_id = product.id
                WHERE 
                    DATE_FORMAT(`order`.date, '%Y-%m') = %s
                GROUP BY 
                    product.id
                ORDER BY 
                    TotalRevenue DESC
            """
            cursor.execute(query, (date,))
            datas = cursor.fetchall()
        else:
            query = """
                SELECT 
                    product.name AS ProductName,
                    product.price AS ProductPrice,
                    SUM(order_item.quantity) AS TotalQuantity,
                    SUM(order_item.quantity * product.price) AS TotalRevenue
                FROM 
                    `order`
                JOIN 
                    order_item ON `order`.id = order_item.order_id
                JOIN 
                    product ON order_item.product_id = product.id
                WHERE 
                    DATE_FORMAT(`order`.date, '%Y') = %s
                GROUP BY 
                    product.id
                ORDER BY 
                    TotalRevenue DESC
            """
            cursor.execute(query, (date,))
            datas = cursor.fetchall()

        detail_dialog = QDialog()
        detail_dialog.setWindowTitle('Chi Tiết Đơn Hàng')
        detail_dialog.setGeometry(100, 100, 600, 400)

        table_widget = QTableWidget()
        table_widget.setColumnCount(4)
        table_widget.setHorizontalHeaderLabels(['Tên sản phẩm', 'Giá', 'Số lượng đã bán', 'Tổng tiền'])
        table_widget.setRowCount(len(datas))
        table_widget.setColumnWidth(0, 200) 
        table_widget.setColumnWidth(1, 100) 
        table_widget.setColumnWidth(2, 100)  
        table_widget.setColumnWidth(3, 150)  
        table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(detail_dialog.accept)
        buttons.rejected.connect(detail_dialog.reject)

        for row_idx, item in enumerate(datas):
            for col_idx, data in enumerate(item):
                if col_idx == 1 or col_idx == 3:
                    data = f"{data}$"
                table_widget.setItem(row_idx,col_idx, QTableWidgetItem(str(data)))

        layout = QVBoxLayout()
        layout.addWidget(table_widget)
        layout.addWidget(buttons)
        detail_dialog.setLayout(layout)

        while True:
            if detail_dialog.exec() == QDialog.Accepted:
                break
            else:
                break
