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


    def __str__(self):
        
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашнее задание: {self.sr_znach():.1f}\n"
                f"Завершенные курсы: {self.get_finished_course()}\n"
                f"Курсы в процессе изучения: {self.get_courses_in_progress()}\n")
    
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
        if (isinstance(student, Student) and 
            course in self.courses_attached and 
            course in student.courses_in_progress):
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}\n"

# Создаем объекты
best_student = Student('Ruoy', 'Gosling', 'Man')
best_student.courses_in_progress += ['Python', 'Java']

cool_reviewer = Reviewer('Cool', 'Reviewer')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']

awesome_lecturer = Lecturer('Awesome', 'Lecturer')
awesome_lecturer.courses_attached += ['Python', 'Java']

# Reviewer выставляет оценки студенту
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Java', 8.7)  

# Студент оценивает лектора
best_student.rate_lector(awesome_lecturer, 'Python', 9)
best_student.rate_lector(awesome_lecturer, 'Java', 7)  # Ошибка: студент не изучает Java

print("Оценки студента:", best_student.grades)
print("Оценки лектора:", awesome_lecturer.grades)



print(best_student)

print(cool_reviewer)

print(awesome_lecturer)



# Студенты с разными баллами
student1 = Student("Anna", "Brown", "Female")
student1.grades = {"Python": [8, 9, 7], "Java": [9, 9]}

student2 = Student("John", "Doe", "Male")
student2.grades = {"Python": [6, 7, 5], "Java": [8, 7]}

# Тестируем операции
print(student1 > student2)   # True (8.4 > 6.6)
print(student1 <= student2)  # False
print(student1 == student2)  # False
print(student1 != student2)  # True

# Лекторы с одинаковым баллом
lecturer1 = Lecturer("Alice", "Smith")
lecturer1.grades = {"Python": [9, 9, 9]}

lecturer2 = Lecturer("Bob", "Johnson")
lecturer2.grades = {"Java": [8, 10, 9]}

print(lecturer1 == lecturer2)  # True (9.0 == 9.0)
print(lecturer1 >= lecturer2)  # True
print(lecturer1 < lecturer2)   # False

student3 = Student("Emma", "Watson", "Female")
student3.grades = {"Python": [10, 10]}

student4 = Student("Tom", "Hanks", "Male")
student4.grades = {"Java": [10, 10]}

print(student3 == student4)  # True (10.0 == 10.0)
print(student3 != student4)  # False
print(student3 >= student4)  # True



