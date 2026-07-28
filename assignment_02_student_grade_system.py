def main():
    def gradeStudent(score):
        if score < 0 and score > 100:
            print("error")
            # score must be between 0 and 100
        elif score >= 80 <=100:
            print("Grade A")
        elif score >=70:
            print("Grade B")
        elif score >=60:
            print("Grade C")
        elif score >=50:
            print(" Grade D")
        else:
            print("Grade F")

    score = int(input("Enter the score: "))
    gradeStudent(score)
main()
        
