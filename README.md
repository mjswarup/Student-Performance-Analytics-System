# Student Performance Analytics System

## 1. Project Overview

The Student Performance Analytics System is a Python-based project designed to analyze student academic performance using Python, NumPy, and Pandas.

The system processes student marks and attendance data, calculates totals and averages, assigns grades, determines pass/fail results, and generates CSV reports.

## 2. Objectives

* Store and process student performance data.
* Calculate total marks and average marks.
* Assign grades based on average marks.
* Determine pass/fail results for each student.
* Analyze class performance and subject-wise averages.
* Identify top-performing students.
* Generate CSV reports for further analysis.

## 3. Technologies Used

* Python
* NumPy
* Pandas
* CSV files
* Visual Studio Code
* Git and GitHub

## 4. Dataset

The sample dataset contains 20 students with the following fields:

* Student ID
* Name
* Department
* Python marks
* Mathematics marks
* Statistics marks
* AI Fundamentals marks
* Data Analysis marks
* Attendance percentage

## 5. Features

* Loads student data using Pandas.
* Uses NumPy for numerical calculations.
* Calculates total and average marks.
* Assigns grades using conditional statements.
* Determines pass/fail status based on subject marks.
* Displays class statistics.
* Calculates subject-wise and department-wise averages.
* Displays the top five performers.
* Exports student results and subject summaries to CSV files.

## 6. Project Structure

```text
Student-Performance-Analytics-System/
├── main.py
├── students.csv
├── README.md
├── Project_Documentation.md
└── outputs/
    ├── student_results.csv
    └── subject_summary.csv
```

## 7. How to Run

1. Install Python.

2. Install the required libraries:

   `python -m pip install pandas numpy`

3. Place `main.py` and `students.csv` in the same folder.

4. Open the project folder in the terminal.

5. Run:

   `python main.py`

6. View the generated CSV reports inside the `outputs` folder.

## 8. Calculation Rules

* Total marks are the sum of the five subject marks.
* Average marks are the total divided by five.
* Grades are assigned according to the average marks.
* A student passes only when every subject mark is at least 35.

## 9. Output Files

* `student_results.csv`: Student details, totals, averages, grades, results, and attendance.
* `subject_summary.csv`: Average marks for each subject.

## 10. Testing

The system was tested using sample student records. Verified cases include a high-performing student, a student failing one subject, a student passing all subjects with a low average, and subject-wise summary generation.

## 11. Conclusion

The project demonstrates Python programming fundamentals, functions, loops, conditional statements, NumPy calculations, Pandas data processing, and CSV report generation.

## 12. Author

Student Name: [Manukonda Jyothi Swarup]

Department: [Computer Science and Engineering]

College: [Avanthi Institute of Engineering & Technology]

GitHub Repository: [Add your repository URL after uploading]
