grade = float(input("Grade /20: "))

if grade < 0 or grade > 20:
    print("Invalid grade: Between 0 and 20")
elif grade >= 16:
    print("Bravo")
elif grade >= 14:
    print("Good")
elif grade >= 12:
    print("Avg")
elif grade >= 10:
    print("Pass")
else:
    print("Fail")