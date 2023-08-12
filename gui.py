import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, \
    QVBoxLayout, QWidget, QHBoxLayout, QTextEdit, QMessageBox
from logic import Logic  # Make sure to import your Logic module correctly


class GradeCalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logic_instance = Logic()

        self.setWindowTitle("Grade Calculator")
        self.setGeometry(100, 100, 250, 450)

        self.main_layout = QVBoxLayout()

        main_label = QLabel("Grade Calculator")
        main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(16)
        main_label.setFont(font)
        self.main_layout.addWidget(main_label)

        self.correction_label = QLabel("")
        self.correction_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(12)
        self.correction_label.setFont(font)
        self.correction_label.setStyleSheet("color: red;")
        self.main_layout.addWidget(self.correction_label)

        self.num_students_label = QLabel("Number of students")
        self.main_layout.addWidget(self.num_students_label)

        self.num_students_input = QLineEdit()
        self.main_layout.addWidget(self.num_students_input)

        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_table)
        self.main_layout.addWidget(self.create_button,alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Student", "Grade"])
        self.main_layout.addWidget(self.table)

        self.button_layout = QHBoxLayout()

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        self.calculate_button = None
        self.clear_button = None
        self.text_box = None

    def create_table(self):
        try:
            num_students = int(self.num_students_input.text())
            if num_students <= 0:
                raise
            self.correction_label.setText("")
        except:
            self.clear_table()
            self.correction_label.setText("Invalid number of students.")

            return

        self.table.setRowCount(num_students)

        for row in range(num_students):
            student_item = QTableWidgetItem()  # Use a local variable instead of instance variable
            self.table.setItem(row, 0, student_item)

            grade_item = QTableWidgetItem()  # Use a local variable instead of instance variable
            self.table.setItem(row, 1, grade_item)

        if not self.calculate_button:
            self.calculate_button = QPushButton("Calculate")
            self.calculate_button.clicked.connect(lambda: self.logic_instance.name_check(self))
            self.button_layout.addWidget(self.calculate_button)

        if not self.clear_button:
            self.clear_button = QPushButton("Clear")
            self.clear_button.clicked.connect(self.clear_table)
            self.button_layout.addWidget(self.clear_button)

        if self.calculate_button and self.clear_button:
            self.main_layout.addLayout(self.button_layout)

        if not self.text_box:
            self.text_box = QTextEdit()
            self.text_box.setPlainText('')
            self.main_layout.addWidget(self.text_box)

    def clear_table(self):
        self.table.clearContents()
        if self.text_box:
            self.text_box.setPlainText('')
        self.correction_label.setText("")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GradeCalculatorApp()
    window.show()
    sys.exit(app.exec())
