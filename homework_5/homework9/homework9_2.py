import csv

def main():
    
    num_students = int(input("Enter the number of students: "))

    
    student_data = []

    
    for i in range(num_students):
        name = input(f"Enter the name of student {i+1}: ")
        score = float(input(f"Enter the score of student {i+1}: "))
        student_data.append([name, score])

    
    with open("student_scores.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Name", "Score"])  # Write header
        csv_writer.writerows(student_data)

    print("Student data has been successfully saved to 'student_scores.csv'.")

if __name__ == "__main__":
    main()
