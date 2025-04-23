class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []  # Студент должен быть записан на курс
        self.grades = {}
        self.lecturer_grades = {}  # Новый атрибут для оценок лекторам

    def rate_lector(self, lecture, course, grade):
        if (isinstance(lecture, Lecturer) and course in self.courses_in_progress 
            and course in lecture.courses_attached):
            lecture.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'
        

    def sr_znach(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades.extend(grade)
        if not all_grades:
            return 0
        sr_grade = (sum(all_grades) / len(all_grades))
        return sr_grade

    def get_finished_course(self):
        if not self.finished_courses:
            return "Нет завершенных курсов"
        return ", ".join(self.finished_courses)
    
    def get_courses_in_progress(self):
        if not self.courses_in_progress:
            return "Нет текущих курсов"
        return ", ".join(self.courses_in_progress)
    
    # Проверка на равенство (==)
    def __eq__(self, other):
        return self.sr_znach() == other.sr_znach()
        
    # Проверка на неравенство (!=)    
    def __ne__(self, other):
        return not (self.sr_znach() == other.sr_znach())
            
        
    # Меньше (<)
    def __lt__(self, other):
        return self.sr_znach() < other.sr_znach()
        
    # Меньше или равно (<=)
    def __le__(self, other):
        return self.sr_znach() < other.sr_znach() or self.sr_znach() == other.sr_znach()


    # Больше (>)
    def __gt__(self, other):
        return self.sr_znach() > other.sr_znach()
    
    # Больше или равно (>=)
    def __ge__(self, other):
        return self.sr_znach() > other.sr_znach() or self.sr_znach() == other.sr_znach()
    



    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашнее задание: {self.sr_znach():.1f}\n"
                f"Завершенные курсы: {self.get_finished_course()}\n"
                f"Курсы в процессе изучения: {self.get_courses_in_progress()}\n")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # Наставник должен быть прикреплен к курсу




class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.grades = {}

    def sr_znach(self):
        all_grade = []
        for grade in self.grades.values():
            all_grade.extend(grade)
        if not all_grade:
            return 0
        return (sum(all_grade) / len(all_grade))

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.sr_znach():.1f}\n")
    
    # Проверка на равенство (==)
    def __eq__(self, other):
        return self.sr_znach() == other.sr_znach()
        
    # Проверка на неравенство (!=)    
    def __ne__(self, other):
        return not (self.sr_znach() == other.sr_znach())
            
        
    # Меньше (<)
    def __lt__(self, other):
        return self.sr_znach() < other.sr_znach()
        
    # Меньше или равно (<=)
    def __le__(self, other):
        return self.sr_znach() < other.sr_znach() or self.sr_znach() == other.sr_znach()


    # Больше (>)
    def __gt__(self, other):
        return self.sr_znach() > other.sr_znach()
    
    # Больше или равно (>=)
    def __ge__(self, other):
        return self.sr_znach() > other.sr_znach() or self.sr_znach() == other.sr_znach()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) 
            and course in self.courses_attached 
            and course in student.courses_in_progress):
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"
    
def average_grades_from_the_entire_course(students, course):
        total_grades = []
        for student in students:
            if course in student.grades:
                total_grades.extend(student.grades[course])
        return sum(total_grades) / len(total_grades)

def calculate_avg_lectures_for_course(lecturers, course_name):
    """Средняя оценка за лекции по курсу у всех лекторов"""
    course_grades = []
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            course_grades.extend(lecturer.grades[course_name])
    return round(sum(course_grades) / len(course_grades), 2) if course_grades else 0

# Создаем студентов
student1 = Student("Emma", "Watson", "Female")
student1.courses_in_progress = ["Python", "JavaScript"]
student1.finished_courses = ["Git"]

student2 = Student("Tom", "Hanks", "Male")
student2.courses_in_progress = ["Python", "Java"]
student2.finished_courses = ["Linux"]

# Создаем проверяющих (Reviewer)
reviewer1 = Reviewer("Alice", "Smith")
reviewer1.courses_attached = ["Python", "JavaScript"]

reviewer2 = Reviewer("Bob", "Brown")
reviewer2.courses_attached = ["Python", "Java"]

# Создаем лекторов (Lecturer)
lecturer1 = Lecturer("John", "Doe")
lecturer1.courses_attached = ["Python"]

lecturer2 = Lecturer("Jane", "Doe")
lecturer2.courses_attached = ["Java", "JavaScript"]


reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student1, "JavaScript", 8)
reviewer2.rate_hw(student2, "Python", 10)
reviewer2.rate_hw(student2, "Java", 7)

student1.rate_lector(lecturer1, "Python", 10)
student2.rate_lector(lecturer2, "Java", 9)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

students_list = [student1, student2]
print("Средняя оценка за домашние задания (Python):", 
      average_grades_from_the_entire_course(students_list, "Python"))

lecturers = [lecturer1, lecturer2]
print("Средняя оценка за лекции по курсу Java:", 
      calculate_avg_lectures_for_course(lecturers, "Java"))