def read_file():
    students_info = {}
    with open("students.txt", "r") as file:
        for line in file:
            info = line.split()
            name = info[0]
            grades = []
            for grade in info[1:]:  # всі елементи окрім першого
                grades.append(int(grade))
            students_info[name] = grades
    return students_info


def processing(students_info):
    student_statistics = {}
    for name, grades in students_info.items():
        student_average_grade = sum(grades) / len(grades)
        st_highest_grade = max(grades)
        st_lowest_grade = min(grades)
        student_statistics[name] = {"Average": student_average_grade, "Highest grade": st_highest_grade, "Lowest grade": st_lowest_grade}

    group_grades = []
    # проходимося по кожному списку оцінок
    for grades in students_info.values():
        # проходимося по кожній оцінці у списку оцінок
        for grade in grades:
            group_grades.append(grade)

    group_average_grade = sum(group_grades) / len(group_grades)
    highest_group_grade = max(group_grades)
    lowest_group_grade = min(group_grades)

    frequency_dictionary = {}  # словник з частотою кожної оцінки
    for grade in group_grades:
        if grade in frequency_dictionary:
            frequency_dictionary[grade] += 1
        else:
            frequency_dictionary[grade] = 1
    max_frequency = max(frequency_dictionary.values())

    # зберігаємо модальні оцінки (найчастіші)
    modes = []
    for grade, frequency in frequency_dictionary.items():
        if frequency == max_frequency:
            modes.append(str(grade))

    mode = ", ".join(modes)

    return student_statistics, group_average_grade, highest_group_grade, lowest_group_grade, mode


def write_stats_to_file(student_statistics, group_average_grade, highest_group_grade, lowest_group_grade, mode):
    with open("statistics.txt", "w") as file:
        for name, stats in student_statistics.items():
            file.write(f"Student: {name}\n"
                       f"Average grade: {stats['Average']}\n"
                       f"Highest grade: {stats['Highest grade']}\n"
                       f"Lowest grade: {stats['Lowest grade']}\n"
                       f"_________________________________________\n")

        file.write(f"Group statistics:\n\n"
                   f"Average grade: {group_average_grade}\n"
                   f"Highest grade: {highest_group_grade}\n"
                   f"Lowest grade: {lowest_group_grade}\n"
                   f"Mode: {mode}")


def main():
    students_data = read_file()
    student_statistics, group_average_grade, highest_group_grade, lowest_group_grade, mode = processing(students_data)
    write_stats_to_file(student_statistics, group_average_grade, highest_group_grade, lowest_group_grade, mode)


main()

