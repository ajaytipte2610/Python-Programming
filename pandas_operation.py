'''
Pandas operation:
    A school maintains student exam scores for multiple subjects. The data is stored in a Pandas DataFrame where each row represents a student, and each column represents a subject.
import pandas as pd
 # Sample data: Student exam scores 
data = { "Math": [85, 78, 92, 60, 74, 88],
 "Science": [80, 82, 89, 65, 70, 90],
  "English": [75, 85, 78, 55, 72, 88], 
  "History": [70, 75, 80, 50, 68, 82] }
 students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5", "Student 6"] exam_scores = pd.DataFrame(data, index=students)
·  Display the first three rows of the exam_scores DataFrame.
·  Get the total number of students and subjects recorded in the DataFrame.
·  List all subject names and student names.
·  Display the data type of each column in the DataFrame.
·  Check if there are any missing values in the DataFrame.
·  Retrieve the scores of "Student 3" in all subjects.
·  Extract the scores of all students in "Math".
·  Retrieve the scores of "Student 1" and "Student 4" in "Science" and "English".
·  Slice the DataFrame to get the first 4 students and the first 3 subjects.
·  Retrieve the score of "Student 5" in "History" using .loc or .iloc.
·  Update the score of "Student 2" in "Math" to 85.
·  Add a new student, "Student 7", with scores [90, 85, 88, 80] for all subjects.
·  Add 5 bonus marks to all students' scores.
·  Deduct 3 marks from the scores of "Student 4" in all subjects.
·  Calculate the percentage of marks obtained by each student, assuming each subject has a maximum of 100 marks.
·  Calculate the total marks obtained by each student.
·  Determine the total marks scored in each subject.
·  Identify the student with the highest total marks.
·  Find the subject with the lowest total marks.
·  Compute the average marks scored by each student across all subjects
'''

import pandas as pd

data = { "Math": [85, 78, 92, 60, 74, 88],
 "Science": [80, 82, 89, 65, 70, 90],
  "English": [75, 85, 78, 55, 72, 88], 
  "History": [70, 75, 80, 50, 68, 82] }

students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5", "Student 6"]
print(students)

exam_scores = pd.DataFrame(data, index=students)
print(exam_scores)

# Q.1
print(exam_scores.head(3))

# Q.2
total_stu = exam_scores.shape[0]
total_sub = exam_scores.shape[1]
print(f"Total number of students {total_stu} , Total number of subjects {total_sub}")

#Q.3
stu_names = exam_scores.index.tolist()
sub_names = exam_scores.columns.tolist()
print("Student Names : " ,stu_names)
print("Subject Names : ",sub_names)

# Q.4
print(exam_scores.dtypes)

#Q.5
print(exam_scores.isnull().sum())

#Q.6
stu_3_scores = exam_scores.loc["Student 3"]
print(stu_3_scores)

#Q.7
math_scores = exam_scores["Math"]
print(math_scores)

# Q.8
s_1_4_s = exam_scores.loc[["Student 1", "Student 4"], ["Science", "English"]]
print(s_1_4_s)

# Q.9 
sliced_data = exam_scores.iloc[:4, :3]
print(sliced_data)

# Q.10 
s_5_h_s = exam_scores.loc["Student 5", "History"]
print(s_5_h_s)

# Q.11.
exam_scores.loc["Student 2", "Math"] = 85
print(exam_scores)

# Q.12 
exam_scores.loc["Student 7"] = [90, 85, 88, 80]
print(exam_scores)

# Q.13
exam_scores = exam_scores + 5
print(exam_scores)

# Q.14
exam_scores.loc["Student 4"] = exam_scores.loc["Student 4"] - 3
print(exam_scores)

# Q.15 
percentage = exam_scores.sum(axis=1) / (exam_scores.shape[1] * 100) * 100
print(percentage)

# Q.16 
total_marks = exam_scores.sum(axis=1)
print(total_marks)

# Q.17 
total_subject = exam_scores.sum(axis=0)
print(total_subject)

#Q.18
highest = total_marks.idxmax()
print(f"Student with the highest total marks: {highest}")

#Q.19
lowest = total_subject.idxmin()
print(f"Subject with the lowest total marks: {lowest}")

#Q.20
average = exam_scores.mean(axis=1)
print(average)