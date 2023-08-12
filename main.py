from PyQt6.QtWidgets import QApplication
from gui import GradeCalculatorApp  # Import your GUI class
from logic import Logic  # Import your Logic class


def main():
    application = QApplication([])
    gui_instance = GradeCalculatorApp()  # Create an instance of the GUI class
    logic_instance = Logic()  # Create an instance of the Logic class

    gui_instance.logic_instance = logic_instance  # Set the logic instance in the GUI

    gui_instance.show()
    application.exec()


if __name__ == '__main__':
    main()
