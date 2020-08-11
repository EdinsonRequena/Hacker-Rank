def main(n, student_marks, query_name):
    one = student_marks[query_name][0]
    two = student_marks[query_name][1]
    three = student_marks[query_name][2]

    result = (one + two + three) / 3

    print("{:.2f}".format(result))


if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    main(n, student_marks, query_name)