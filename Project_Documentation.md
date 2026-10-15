# Student Performance Analytics System

## 1. Project Title
**Student Performance Analytics System Using Python, NumPy, and Pandas**

## 2. Student Details
- **Student Name:** Jyothi Swarup
- **Course:** B.Tech
- **Department:** Update with your department
- **Project Type:** Academic Mini Project
- **Submission Date:** 15 October 2026
- **GitHub Repository:** https://github.com/mjswarup/Student-Performance-Analytics-System

## 3. Introduction
The Student Performance Analytics System is a Python-based project developed to analyze student academic performance. It processes student details, subject marks, and attendance data to calculate totals, averages, grades, and pass/fail results.

The project uses Pandas for dataset handling and analysis and NumPy for numerical calculations. It generates summary reports that help identify top-performing students and understand overall class performance.

## 4. Problem Statement
Manually calculating student marks, averages, grades, and class statistics can be time-consuming and may lead to calculation errors. A simple automated system is needed to process student data accurately and generate useful academic performance reports.

## 5. Objectives
- Store student information in a CSV dataset.
- Load and process data using Pandas.
- Perform numerical calculations using NumPy.
- Calculate total marks and average marks for each student.
- Assign grades based on average marks.
- Determine pass/fail results using subject-wise pass criteria.
- Identify the highest and lowest student averages.
- Calculate subject-wise and department-wise averages.
- Identify the top five performers.
- Export analysis results into CSV reports.

## 6. Technologies Used
- **Programming Language:** Python
- **Data Manipulation:** Pandas
- **Numerical Computation:** NumPy
- **Dataset Format:** CSV
- **Development Environment:** Visual Studio Code
- **Version Control:** Git
- **Repository Hosting:** GitHub

## 7. Dataset Description
The project uses `students.csv`, which contains records for 20 sample students.

The dataset contains the following fields:

| Field | Description |
|---|---|
| Student_ID | Unique student identifier |
| Name | Student name |
| Department | Student's department |
| Python | Marks in Python |
| Mathematics | Marks in Mathematics |
| Statistics | Marks in Statistics |
| AI_Fundamentals | Marks in AI Fundamentals |
| Data_Analysis | Marks in Data Analysis |
| Attendance | Attendance percentage |

Subject marks and attendance are represented on a scale of 0 to 100.

## 8. Implementation

### 8.1 Data Loading
The system uses Pandas `read_csv()` to load student records from `students.csv` into a DataFrame.

It checks whether the required columns are present, whether the dataset contains records, whether student IDs are duplicated, and whether marks and attendance values fall within the valid range.

### 8.2 Total Marks Calculation
The total marks are calculated by adding the marks obtained in all five subjects.

**Formula:**

Total Marks = Python + Mathematics + Statistics + AI Fundamentals + Data Analysis

The system uses NumPy's `sum()` function to calculate total marks.

### 8.3 Average Marks Calculation
The average is calculated by dividing the total marks by the number of subjects.

**Formula:**

Average Marks = Total Marks / 5

NumPy's `mean()` function is used for this calculation.

### 8.4 Grade Assignment
The system assigns grades according to the following rules:

| Average Marks | Grade |
|---|---|
| 90 and above | A+ |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| 50 to below 60 | D |
| Below 50 | F |

Python conditional statements are used to assign the appropriate grade.

### 8.5 Pass/Fail Evaluation
A student passes when the marks in **every subject are at least 35**.

If the student scores below 35 in even one subject, the result is Fail.

The system uses Pandas conditions and NumPy's `where()` function to determine each student's result.

### 8.6 Performance Analysis
The system calculates:
- Total number of students.
- Class average.
- Highest student average.
- Lowest student average.
- Number of students who passed and failed.
- Average marks for each subject.
- Top five students based on average marks.
- Department-wise average performance.

### 8.7 Report Generation
The system creates an `outputs` directory if it does not already exist and saves two reports:

1. `student_results.csv` — contains student details, marks, totals, averages, grades, and results.
2. `subject_summary.csv` — contains subject names and their average marks.

## 9. Project Features
- Automated academic calculations.
- Data validation before analysis.
- Total and average marks calculation.
- Grade assignment.
- Pass/fail classification.
- Subject-wise analysis.
- Department-wise analysis.
- Top five performer identification.
- CSV report generation.
- Reusable functions for better code organization.

## 10. Testing and Results
The program was executed successfully using the sample student dataset.

The following cases were checked:

- **High-performing student:** Meera (S004) obtained a total of 474 marks, an average of 94.8, grade A+, and result Pass.
- **Student failing a subject:** Arjun (S005) obtained an average of 37.4 and result Fail because the Python mark was 32, below the required subject pass mark of 35.
- **Student passing with a low average:** Manoj (S018) obtained an average of 38.2 and result Pass because all five subject marks were at least 35.

The program also generated the student results and subject summary CSV reports.

## 11. Output Files
The generated output files are stored in the `outputs` folder.

- `outputs/student_results.csv`
- `outputs/subject_summary.csv`

Screenshots of the program execution and generated reports should be included in the project's `screenshots` folder, if available.

## 12. How to Run the Project

### Prerequisites
- Python installed on the computer.
- Pandas and NumPy installed.

### Installation
Open a terminal in the project folder and run:

```bash
python -m pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```text
pandas
numpy
```

### Execution
Run the following command:

```bash
python main.py
```

The system displays performance analysis in the terminal and saves the CSV reports in the `outputs` folder.

## 13. Challenges and Learning Outcomes

### Challenges
- Organizing student data in a structured format.
- Validating input data before calculations.
- Applying grade and pass/fail conditions correctly.
- Performing numerical calculations across multiple subjects.
- Generating output reports automatically.

### Learning Outcomes
Through this project, I learned how to:
- Use Python variables, data types, conditions, loops, and functions.
- Read and process CSV files using Pandas.
- Perform numerical calculations using NumPy.
- Analyze data using averages, maximum values, minimum values, and grouping.
- Export processed data to CSV files.
- Use Git and GitHub for project version control and submission.

## 14. Future Enhancements
Possible future improvements include:
- Interactive charts and dashboards.
- Graphical comparison of student and subject performance.
- Attendance-based alerts.
- A web-based interface for teachers and students.
- Database integration for larger datasets.
- Predictive analytics for identifying students who may need academic support.

These are proposed enhancements and are not part of the current implementation.

## 15. Conclusion
The Student Performance Analytics System demonstrates how Python, NumPy, and Pandas can be used to automate student performance calculations and analyze academic data. It calculates total marks, averages, grades, and pass/fail results, identifies top performers, and generates reusable CSV reports.

This project provides practical experience in Python programming, data processing, numerical computation, data analysis, and version control.

## 16. GitHub Repository
**Repository URL:** https://github.com/mjswarup/Student-Performance-Analytics-System

The repository contains the project source code, dataset, documentation, and generated reports as uploaded.

## 17. Screenshots
Insert screenshots of the following:
1. Program execution in the terminal.
2. Student results report.
3. Subject summary report.
4. GitHub repository showing the uploaded project files.
