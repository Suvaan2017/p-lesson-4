print("enter marks obtained in 4 subjects:")
marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))
marks4 = int(input("Enter marks for subject 4: "))

total_marks = marks1 + marks2 + marks3 + marks4
print ("sum of 4 subjects is:", total_marks)
perc = (total_marks / 400) * 100
print(end=" percentage is: ")
print(perc)

