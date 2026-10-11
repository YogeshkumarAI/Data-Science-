import pandas as pd
import numpy as np


df = pd.read_csv("MiniProjects/Student_Dataset.csv")

# student analyzer;
class studentAnalyzer:
    @staticmethod
    def TotalStudents():
        print(f"Total Students: {df.shape[0]}")

    @staticmethod
    def AvgMarksInMaths():
        print(f"Average Math Grade: {df['math.grade'].mean():.2f}")

    @staticmethod
    def AvgMarksInEnglish():
        print(f"Average English Grade: {df['english.grade'].mean():.2f}")

    @staticmethod
    def AvgMarksInScience():
        print(f"Average Science Grade: {df['sciences.grade'].mean():.2f}")

    @staticmethod
    def AvgMarksInLanguage():
        print(f"Average Language Grade: {df['language.grade'].mean():.2f}")

    @staticmethod
    def AvgMarksInPortfolio():
        print(f"Average Portfolio Rating: {df['portfolio.rating'].mean():.2f}")

    @staticmethod
    def AvgMarksInCoverLetter():
        print(f"Average Cover Letter Rating: {df['coverletter.rating'].mean():.2f}")

    @staticmethod
    def AvgMarksInRefLetter():
        print(f"Average Reference Letter Rating: {df['refletter.rating'].mean():.2f}")

    @staticmethod
    def HighestScorer():
        subjects = [
            "math.grade",
            "english.grade",
            "sciences.grade",
            "language.grade",
            "portfolio.rating",
            "coverletter.rating",
            "refletter.rating"
        ]

        highest_grade = df[subjects].max().max()

        print("\nHighest Scorer:")

        for subject in subjects:
            matching_rows = df[df[subject] == highest_grade]

            for _, student in matching_rows.iterrows():
                print(f"Name: {student['name']}")
                print(f"Subject: {subject}")
                print(f"Grade: {student[subject]}")

    @staticmethod
    def LowestScorer():
        subjects = [
            "math.grade",
            "english.grade",
            "sciences.grade",
            "language.grade",
            "portfolio.rating",
            "coverletter.rating",
            "refletter.rating"
        ]

        lowest_grade = df[subjects].min().min()

        print("\nLowest Scorer:")

        for subject in subjects:
            matching_rows = df[df[subject] == lowest_grade]

            for _, student in matching_rows.iterrows():
                print(f"Name: {student['name']}")
                print(f"Subject: {subject}")
                print(f"Grade: {student[subject]}")

    @staticmethod
    def AverageGrade():
        subjects = [
            "math.grade",
            "english.grade",
            "sciences.grade",
            "language.grade",
            "portfolio.rating",
            "coverletter.rating",
            "refletter.rating"
        ]

        df["average.grade"] = df[subjects].mean(axis=1)

        print("\nAverage Grade per Student:")

        print(df[["name", "average.grade"]].head())




# ========== Studentanalyzer ==========
print("========== Studentanalyzer ==========")
while(True):
    print("1. TotalStudents")
    print("2. Maths Avgrage")
    print("3. English Avgrage")
    print("4. Science Avgrage")
    print("5. Language Avgrage")
    print("6. Portfolio Avgrage")
    print("7. CoverLetter Avgrage")
    print("8. Refletter Avgrage")
    print("9. Highest Scorer with marks")
    print("10. Lowest Scorer with marks")
    print("11. Average Scorer with marks")

    n = int(input("Enter Your Command: "))

    match n:
        case 1:
            studentAnalyzer.TotalStudents()
            break

        case 2:
            studentAnalyzer. AvgMarksInMaths()
            break

        case 3:
            studentAnalyzer. AvgMarksInEnglish()
            break

        case 4:
            studentAnalyzer. AvgMarksInScience()
            break

        case 5:
            studentAnalyzer. AvgMarksInLanguage()
            break

        case 6:
            studentAnalyzer. AvgMarksInPortfolio()
            break

        case 7:
            studentAnalyzer. AvgMarksInCoverLetter()
            break

        case 8:
            studentAnalyzer. AvgMarksInRefLetter()
            break
        
        case 9:
            studentAnalyzer. HighestScorer()
            break

        case 10:
            studentAnalyzer. LowestScorer()
            break

        case 11:
            studentAnalyzer. AverageGrade()
            break

        case "0": 
            print("Thank you for using Student Analyzer!") 
            break 

        case _: 
            print("Invalid choice! Please enter a number from 0 to 11.")







