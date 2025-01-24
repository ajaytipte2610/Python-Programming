'''
A school maintains a record of students' exam scores for 5 subjects in a 2D NumPy array. Each row represents a student, and each column represents a subject:    import numpy as np      # Student scores: rows = students, columns = subjects      scores = np.array([    [85, 90, 78, 92, 88],   # Student 1    [72, 75, 80, 68, 74],   # Student 2    [95, 88, 92, 96, 90],   # Student 3    [60, 65, 70, 58, 62],   # Student 4    [88, 84, 86, 89, 87]    # Student 5 ])     
1.Retrieve the scores of Student 3 for all subjects.
 2.Retrieve the scores for Subject 2 (column 2) across all students.
  3.Extract the scores of the first 3 students for the first 2 subjects.Extract the scores of the last 2 students for the last 3 subjects. 
  4.Add 5 bonus marks to all scores. 
  5.Subtract 10 marks from scores of Subject 4 for all students.
   6.Calculate the percentage scores of each student assuming each subject is out of 100. 
   7.Calculate the average score for each student across all subjects. 
   8.Find the total marks scored by each student. 
   9.Identify the highest score in the entire array. 
   10.Determine the average score for each subject. 
   11.Find the student with the lowest average score.
   '''



import numpy as np

scores = np.array([
    [85, 90, 78, 92, 88],  
    [72, 75, 80, 68, 74],  
    [95, 88, 92, 96, 90],  
    [60, 65, 70, 58, 62],  
    [88, 84, 86, 89, 87]   
])


# Q1 

stu_3_scores = scores[2,:]
print("subject 3 scores : ",stu_3_scores)


# Q2

sub_2 = scores[:,2]
print(" subject 2scores : ",sub_2)

# Q3

first_3_students_first_2_subjects = scores[:3, :2]
print("First 2 students of first 2 subjects scores : ",first_3_students_first_2_subjects)


last_2_students_last_3_subjects = scores[3:, 2:]
print("Lat 2 students last 3 subjects scores : ",last_2_students_last_3_subjects)


# Q4

bonus_scores = scores + 5
print("Bonuas scores : ",bonus_scores)

# Q5

scores[:,3] -= 10
print("After substracting 10 from subject 4 scores : ",scores)

#Q6

total_possible_marks = 5 * 100
percentages = (scores.sum(axis=1) / total_possible_marks) * 100
print("Percentage : ",percentages)

# Q7

average_scores = scores.mean(axis=1)
print("Average scores : ",average_scores)

#Q8

total_marks = scores.sum(axis=1)
print("Total marks : ",total_marks)

# Q9

highest_score = np.max(scores)
print("Highest score : ",highest_score)

# Q10

average_subject_scores = scores.mean(axis=0)
print("Average subject score : ",average_subject_scores)


# Q11

lowest_avg_student = np.argmin(average_scores)
print("Lowest average student : ",lowest_avg_student)
