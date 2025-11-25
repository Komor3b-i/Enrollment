class Course:
    def __init__(self, name,  department, units):
        self.name = name
        self.department = department
        self.units = units


class DegreeProgram:
    def __init__(self, name, department):
        self.name = name
        self.department = department


class AcademicDepartment:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, fname, lname, year, degreeProgram,prevSemesterGrade):
        self.fname = fname
        self.lname = lname
        self.year = year
        self.degreeProgram = degreeProgram
        self.previous_semester_grade =prevSemesterGrade
        self.courses = []
        self.max_units = self.set_max_units()

    def set_max_units(self):
        if self.year in [1, 2]:
            return 27
        elif self.year == 3:
            return 24
        elif self.year == 4:
            return 12
        else:
            return 0

    def enroll_course(self, course):
        total_units = sum(tunits.units for tunits in self.courses)
        if total_units + course.units <= self.max_units:
            self.courses.append(course)
            print(f" {self.fname } {self.lname} Enrolled in {course.name} successfully.")
        else:
            print(f"Cannot enroll. Unit limit exceeded. You can only enroll {self.max_units} units")

    def display_courses(self):
        if self.courses:
            print(f"Courses enrolled by {self.fname} {self.lname}:")
            for course in self.courses:
                print(f"- {course.name} ({course.units} units)")
        else:
            print("No courses enrolled yet.")


class StudentAthlete(Student):
    def __init__(self, fname, lname, year, degreeProgram,prevSemesterGrade, trainingSched, AP, sport):
        super().__init__(fname, lname, year, degreeProgram,prevSemesterGrade)
        self.trainingSched = trainingSched
        self.AP = AP
        self.sport = sport

    def display_trainingSched(self):
        print(f"Training Schedule for {self.fname} {self.lname} : {self.trainingSched} : {self.sport}")

    def calculate_discount(self):
        if self.AP > 85:
            return 100
        elif self.AP > 70:
            return 75
        elif self.AP > 50:
            return 50
        else:
            return 0


class AcademicScholar(Student):
    def display_scholar_grade(self):
        print(f"Scholar Grade for {self.fname} {self.lname}: {self.previous_semester_grade}")

    def check_eligibility(self):
        if self.previous_semester_grade < 1.15:
            return 100
        elif self.previous_semester_grade < 1.25:
            return 75
        elif self.previous_semester_grade < 1.35:
            return 50
        else:
            return 0

cs_department = AcademicDepartment("School of Computer Studies")
cs_course1 = Course("CS Elec 2", cs_department, 3)
cs_course2 = Course("CS Elec 3",  cs_department, 3)
cs_course3 = Course("Appsdev",  cs_department, 3)
cs_course4 = Course("Research",  cs_department, 3)
calculus_course = Course("Calculus", cs_department, 3)

eg_department = AcademicDepartment("Department of Engineering")
eg_course1 = Course("Introduction to Engineering", eg_department, 3)
eg_course2 = Course("EG50", eg_department, 3)
eg_course3 = Course("ADV calculus", eg_department, 3)

csdegreeprogram = DegreeProgram("Computer Science", cs_department)
egdegreeprogram = DegreeProgram("Civil Engineering", eg_department)




student1 = Student("Larry", "Catamco", 4, csdegreeprogram, 1.3)
student1.enroll_course(cs_course1)
student1.enroll_course(cs_course2)
student1.enroll_course(cs_course3)
student1.enroll_course(cs_course4)
student1.enroll_course(calculus_course)
student1.display_courses()

athlete = StudentAthlete("Paulo", "Gabriel", 1, egdegreeprogram, 1.8, "Mon, Wed, Fri - 5 PM to 7 PM", 90, "Basketball")
athlete.display_trainingSched()
print(f"Athletic Discount: {athlete.calculate_discount()}%")

scholar = AcademicScholar("Elijah", "Villafuerte", 3, csdegreeprogram, 1.1)
scholar.display_scholar_grade()
print(f"Scholarship Discount: {scholar.check_eligibility()}%")
