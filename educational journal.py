class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def estimation(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def ave_est(self):
        for course, estimation in self.grades.items():
            res = sum(estimation) / len(estimation)
            return res

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.ave_est():.2f}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.ave_est() > other.ave_est()

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.ave_est() == other.ave_est()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def ave_est(self):
        for course, estimation in self.grades.items():
            res = sum(estimation) / len(estimation)
            return res

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.ave_est():.2f}'


class Reviewer(Mentor):
    def estimation(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def student_rating(list_, course_name):
    sum_all = 0
    count_all = 0
    for stud in list_:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.ave_est()
            count_all += 1
        else:
            return
    average_for_all = sum_all / count_all
    return f"Средняя оценка для всех студентов на курсе {course_name}: {average_for_all:.2f}"


def lecturer_rating(list_, course_name):
    sum_all = 0
    count_all = 0
    for lect in list_:
        if lect.courses_attached == [course_name]:
            sum_all += lect.ave_est()
            count_all += 1
        else:
            return
    average_for_all = sum_all / count_all
    return f"Средняя оценка для всех лекторов по курсу {course_name}: {average_for_all:.2f}"


peter = Student('Peter', 'Dinklage', 'Man')
peter.finished_courses += ['GIt']
peter.courses_in_progress += ['Python']

lena = Student('Lena', 'Kathren', 'Woman')
lena.finished_courses += ['1C']
lena.courses_in_progress += ['Python']

emi = Lecturer('Emilia', 'Clarke')
emi.courses_attached += ['Python']

kit = Lecturer('Christopher', 'Harington')
kit.courses_attached += ['Python']

soph = Reviewer('Sophie', 'Jonas')
soph.courses_attached += ['Python']

john = Reviewer('John', 'Bradley')
john.courses_attached += ['Python']

soph.estimation(peter, 'Python', 9)
soph.estimation(peter, 'Python', 10)
soph.estimation(peter, 'Python', 7)

john.estimation(lena, 'Python', 8)
john.estimation(lena, 'Python', 7)
john.estimation(lena, 'Python', 10)

peter.estimation(emi, 'Python', 10)
peter.estimation(emi, 'Python', 9)
peter.estimation(emi, 'Python', 10)

lena.estimation(kit, 'Python', 8)
lena.estimation(kit, 'Python', 9)
lena.estimation(kit, 'Python', 9)

study_list = [peter, lena]
lect_list = [emi, kit]

print(soph.__str__(), "\n")
print(john.__str__(), "\n")
print(emi.__str__(), "\n")
print(kit.__str__(), "\n")
print(peter.__str__(), "\n")
print(lena.__str__(), "\n")
print(peter.__eq__(kit), "\n")
print(lena.__lt__(emi), "\n")
print(student_rating(study_list, 'Python'), "\n")
print(lecturer_rating(lect_list, 'Python'), "\n")


