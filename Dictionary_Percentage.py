if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l = len(student_marks[query_name])
    s=0
    for i in range(0,l):
        s+=student_marks[query_name][i]
    print("{0:.2f}".format(s/3))