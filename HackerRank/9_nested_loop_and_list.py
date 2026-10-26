if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        students.append([name, grade])

    grades = []
    for student in students:
        for item in student:
            if isinstance(item, float):
                grades.append(item)

    lowest_grade = sorted(grades)[0]

    higher_grades = [grade for grade in grades if grade!=lowest_grade ]
    
    second_lowest_grade = sorted(higher_grades)[0]
    
    matching_students = [student for student in students if second_lowest_grade in student]
    
    matching_names = [student[0] for student in matching_students]

    for name in sorted(matching_names):
        print(name)