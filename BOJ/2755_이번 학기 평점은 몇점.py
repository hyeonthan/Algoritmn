import sys

grades = {'A+':4.3, 'A0':4, 'A-':3.7, 'B+':3.3, 'B0':3.0,
         'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7,
         'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}

grade = 0
grade_score = 0
N = int(input())
for _ in range(N) :
    _, input_grade, input_grade_score = map(str, sys.stdin.readline().split())
    grade += int(input_grade)
    grade_score += float(input_grade) * grades[input_grade_score]

print(round(grade_score/grade + 0.001, 2))