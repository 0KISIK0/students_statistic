def calculate_average(grades):
    res = sum(grades)/len(grades)
    return res
def count_grades(grades,target_grade):
    target = 0
    for grade in grades:
        if grade == target_grade:
            target+=1
    return target

def get_perfomance_category(average):
    if average < 2.5:
        return "Неуспевающий"
    elif average >= 2.5 and average < 3.5:
        return "Троечник"
    elif average >= 3.5 and average < 4.5:
        return "Хорошист"
    elif average >= 4.5:
        return "Отличник"

def check(grades):
    res = 0
    for grade in grades:
        if grade == 2:
            res+=1
    if res > 0:
        print("Студент под угрозой отчисления!")
    else:
        print("Все в порядке")

def sorted(grades):
    res = sorted(grades)
    return res

def split_text(str_grades):
    list_grade = []
    split_grade = str_grades.split(" ")
    for i in split_grade:
        res = int(i)
        list_grade.append(res)
    return list_grade

count_students = int(input("Введите число студентов: "))
cnt = 0
cnt1 = 0
for i in range(count_students):
    students_grade = split_text(input("Введите оценки студента. Пример: '4 5 3 2': "))
    average = calculate_average(students_grade)
    cnt1+=average
    print(calculate_average(students_grade))
    print(count_grades(students_grade,5))
    print(get_perfomance_category(average))
    if get_perfomance_category(average) == "Отличник":
        cnt+=1
print(cnt)
print(cnt1/count_students)

