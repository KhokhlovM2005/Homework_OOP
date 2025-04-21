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

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and 
            course in self.courses_attached and 
            course in student.courses_in_progress):
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

# Создаем объекты
best_student = Student('Ruoy', 'Gosling', 'Man')
best_student.courses_in_progress += ['Python', 'Java']

cool_reviewer = Reviewer('Cool', 'Reviewer')
cool_reviewer.courses_attached += ['Python']

awesome_lecturer = Lecturer('Awesome', 'Lecturer')
awesome_lecturer.courses_attached += ['Python']

# Reviewer выставляет оценки студенту
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Java', 8)  # Ошибка: Reviewer не прикреплен к Java

# Студент оценивает лектора
best_student.rate_lector(awesome_lecturer, 'Python', 9)
best_student.rate_lector(awesome_lecturer, 'Java', 7)  # Ошибка: студент не изучает Java

print("Оценки студента:", best_student.grades)
print("Оценки лектора:", awesome_lecturer.grades)