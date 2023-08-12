import csv

class Logic:
    def __init__(self):
        self.student_data = {}

    def name_check(self, gui_instance):
        print("Name check logic executed")

        # Clear previous corrections
        gui_instance.correction_label.setText("")

        # get student name and grade
        for row in range(gui_instance.table.rowCount()):
            student_name_item = gui_instance.table.item(row, 0)
            grade_item = gui_instance.table.item(row, 1)

            student_name = student_name_item.text().strip()
            grade_text = grade_item.text()

            #invalid inputs
            if student_name == "":
                gui_instance.correction_label.setText("Student name cannot be empty.")
                return
            if student_name in self.student_data:
                gui_instance.correction_label.setText("Duplicate student names.")
                return
            #invalid inputs
            try:
                grade = int(grade_text)
                if grade < 0:
                    gui_instance.correction_label.setText("Negative grades not allowed.")
                    return
            except ValueError:
                gui_instance.correction_label.setText("Invalid grade input.")
                return

            self.student_data[student_name] = grade
        print(self.student_data)
        print("made it")
        self.save_to_csv(gui_instance)

    def save_to_csv(self, gui_instance, filename='student_data.csv'):
        max_grade = max(self.student_data.values())
        grade_mapping = {
            'A': max_grade - 10,
            'B': max_grade - 20,
            'C': max_grade - 30,
            'D': max_grade - 40,
            'F': max_grade - 50
        }

        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Student Name', 'Grade', 'Adjusted Grade'])

            for student_name, grade in self.student_data.items():
                adjusted_grade = self.get_adjusted_grade(grade, grade_mapping)
                csv_writer.writerow([student_name, grade, adjusted_grade])

                #text box writting
                gui_instance.text_box.append(f"{student_name} score is {grade} and grade is {adjusted_grade}\n")

    @staticmethod
    def get_adjusted_grade(grade, grade_mapping):
        for letter_grade, threshold in grade_mapping.items():
            if grade >= threshold:
                return letter_grade
        return 'F'


