class student:
    def __init__(std):
        std.name =""
        std.roll = 0
        std.marks = 0.0
    def input_details(std):
        std.name = input("Enter student name:")
        std.roll = input("Enter student roll no:")
        std.marks = float(input("Enter student marks:"))
    def display_details(std):
        print("\n student details")
        print(f"name {std.name}")
        print(f"roll {std.roll}")
        print(f"marks {std.marks}")

student1 = student()
student1.input_details()
student1.display_details()




        