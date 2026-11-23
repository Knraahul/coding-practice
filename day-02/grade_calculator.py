name= input("Enter vthe name of the student:")
grade= int(input("Enter the grade of the student:"))
if grade >=90:
    print(name, "Has passed with A grade")
elif grade>=80 and grade<90:
    print(name, "Has passed with B grade")
elif grade>=70 and grade<80:
    print(name, "Has passed with C grade")
elif grade>=60 and grade<70:
    print(name, "Has passed with D grade")
elif grade>=50 and grade<60:
    print(name, "Has passed with E grade")    
else:
    print(name, "Has failed the exam")                