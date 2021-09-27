def check_exam(arr1, arr2):
    score = 0
    for correct_answer, student_answer in zip(arr1, arr2):
        if correct_answer == student_answer:
            score += 4
        if check_input(student_answer) and correct_answer != student_answer:
            score -= 1
    if score < 0:
        score = 0
    return score


def check_input(number):
    if number is None or number == "":
        return False
    return True

