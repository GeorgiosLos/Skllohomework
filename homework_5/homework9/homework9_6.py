import csv
import json

def calculate_average(scores):
    return sum(scores.values()) / len(scores)

def main():
    
    with open("/home/hp/Skillohomework/homework_5/homework9/data.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        
       
        for row in reader:
            student_name = row['Name']
            exam_scores_json = row['ExamScores']
            exam_scores = json.loads(exam_scores_json)
            average_score = calculate_average(exam_scores)
            
            print(f"{student_name}: Average score = {average_score}")

if __name__ == "__main__":
    main()
