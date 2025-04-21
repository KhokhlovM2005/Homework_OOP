class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []  # Студент должен быть записан на курс
        self.grades = {}

    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # Наставник должен быть прикреплен к курсу

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and 
            course in self.courses_attached and 
            course in student.courses_in_progress):
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'
        
class Lecture(Mentor):
    pass

class Reviewer(Mentor):
    pass

# Создаем объекты
best_student = Student('Ruoy', 'Gosling', 'Man')
best_student.courses_in_progress += ['Python', 'Java', 'Js']  # Добавляем все курсы

cool_mentor = Mentor('Cool', 'Teacher')
cool_mentor.courses_attached += ['Python', 'Java', 'Js']  # Единый регистр

# Проставляем оценки
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Java', 9)
cool_mentor.rate_hw(best_student, 'Js', 8)

print(best_student.grades) 
# Вывод: {'Python': [10], 'Java': [9], 'Js': [8]}