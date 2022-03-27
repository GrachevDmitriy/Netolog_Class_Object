class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    # Реализация __str__ Student
    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе изучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res
    # Выставление оценок лекторам

    def rate_hw(self, lecturer, course, grade):

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('not found')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    # Выставление оценок студентам
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    # Реализация __str__ Reviewer

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    # Сравнение лекторов
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('not found')
            return
        return self.average_rating < other.average_rating

    #     Реализация __str__ Lecturer
    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res


# Создаем лекторов и закрепляем их за курсом
best_lecturer_1 = Lecturer('Benedikt', 'Kozar')
best_lecturer_1.courses_attached += ['Html']

best_lecturer_2 = Lecturer('Igor', 'Krutoy')
best_lecturer_2.courses_attached += ['Python']

best_lecturer_3 = Lecturer('Yaroslav', 'Zaycev')
best_lecturer_3.courses_attached += ['Python']

#  Reviewer их за курсы
cool_reviewer_1 = Reviewer('Bill', 'Kotov')
cool_reviewer_1.courses_attached += ['Html']
cool_reviewer_1.courses_attached += ['Python']

cool_reviewer_2 = Reviewer('Adom', 'Sendler')
cool_reviewer_2.courses_attached += ['Html']
cool_reviewer_2.courses_attached += ['Python']

# Студенты и курсы
student_1 = Student('Denis', 'Tretyakov')
student_1.courses_in_progress += ['Html']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Danila', 'Bogrov')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Alex', 'Volkov')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

# Оценки лекторам за лекции
student_1.rate_hw(best_lecturer_1, 'Html', 10)
student_1.rate_hw(best_lecturer_1, 'Html', 5)
student_1.rate_hw(best_lecturer_1, 'Html', 9)

student_1.rate_hw(best_lecturer_2, 'Python', 10)
student_1.rate_hw(best_lecturer_2, 'Python', 7)
student_1.rate_hw(best_lecturer_2, 'Python', 10)

student_1.rate_hw(best_lecturer_1, 'Html', 7)
student_1.rate_hw(best_lecturer_1, 'Html', 10)
student_1.rate_hw(best_lecturer_1, 'Html', 7)

student_2.rate_hw(best_lecturer_2, 'Python', 8)
student_2.rate_hw(best_lecturer_2, 'Python', 10)
student_2.rate_hw(best_lecturer_2, 'Python', 9)

student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 10)
student_3.rate_hw(best_lecturer_3, 'Python', 6)

# Оценки студентам за ДЗ
cool_reviewer_1.rate_hw(student_1, 'Html', 8)
cool_reviewer_1.rate_hw(student_1, 'Html', 9)
cool_reviewer_1.rate_hw(student_1, 'Html', 10)

cool_reviewer_2.rate_hw(student_2, 'Python', 8)
cool_reviewer_2.rate_hw(student_2, 'Python', 10)
cool_reviewer_2.rate_hw(student_2, 'Python', 9)

cool_reviewer_2.rate_hw(student_3, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)
cool_reviewer_2.rate_hw(student_3, 'Python', 9)


# Оцененые студенты
print(f'\nПеречень студентов:\n{student_1}\n\n{student_2}\n\n{student_3}')

# Оцененые лекторы
print(f'\nПеречень лекторов:\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')



# Сравнения студентов по средним оценкам за ДЗ
print(f'\nСравнения студентов (по средним оценкам за ДЗ):\n '
      f'{student_2.name} {student_2.surname} < {student_3.name} {student_3.surname} = {student_2 < student_3}\n')


# Сравнения лекторов по средним оценкам за лекции
print(f'\nСравнения лекторов (по средним оценкам за лекции): '
      f'\n{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}\n')



#  Список студентов
student_list = [student_1, student_2, student_3]

#  Подсчет средней оценки студентов

def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

print(f"\nСредняя оценка студентов по курсу {'Html'}: {student_rating(student_list, 'Html')}\n")


# Список лекторов
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]

#  Подсчет средней оценки лекторов
def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all
print(f"Средняя оценка лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")









