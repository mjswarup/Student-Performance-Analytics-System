
import pandas as pd
import numpy as np
from pathlib import Path

# Project settings
DATA_FILE = "students.csv"
OUTPUT_DIR = Path("outputs")

SUBJECTS = [
    "Social",
    "Mathematics",
    "English",
    "Physics",
    "Chemistry"
]

PASS_MARK = 35


def load_data():
    """Read and validate student data."""
    df = pd.read_csv(DATA_FILE)

    required_columns = [
        "Student_ID", "Name", "Department",
        *SUBJECTS, "Attendance"
    ]

    missing = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    if df.empty:
        raise ValueError("The dataset contains no students.")

    if df["Student_ID"].duplicated().any():
        raise ValueError("Duplicate student IDs found.")

    for column in SUBJECTS + ["Attendance"]:
        df[column] = pd.to_numeric(df[column], errors="raise")

        if not df[column].between(0, 100).all():
            raise ValueError(
                f"{column} values must be between 0 and 100."
            )

    return df


def calculate_results(df):
    """Calculate total, average, grade and pass/fail."""
    df = df.copy()

    # NumPy calculations
    marks = df[SUBJECTS].to_numpy(dtype=float)

    df["Total"] = np.sum(marks, axis=1)
    df["Average"] = np.mean(marks, axis=1)

    # Assign grades using conditions and a loop
    grades = []

    for average in df["Average"]:
        if average >= 90:
            grades.append("A+")
        elif average >= 80:
            grades.append("A")
        elif average >= 70:
            grades.append("B")
        elif average >= 60:
            grades.append("C")
        elif average >= 50:
            grades.append("D")
        else:
            grades.append("F")

    df["Grade"] = grades

    # A student must score at least 35 in every subject
    passed = (df[SUBJECTS] >= PASS_MARK).all(axis=1)

    df["Result"] = np.where(passed, "Pass", "Fail")

    return df


def show_analysis(df):
    """Display student and class performance."""

    print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 55)

    print("\n1. STUDENT RESULTS")

    columns = [
        "Student_ID", "Name", "Department",
        "Total", "Average", "Grade", "Result", "Attendance"
    ]

    print(df[columns].round(2).to_string(index=False))

    print("\n2. CLASS STATISTICS")
    print("-" * 35)

    print("Total students:", len(df))
    print(f"Class average: {df['Average'].mean():.2f}")
    print(f"Highest average: {df['Average'].max():.2f}")
    print(f"Lowest average: {df['Average'].min():.2f}")

    passed_count = (df["Result"] == "Pass").sum()
    failed_count = (df["Result"] == "Fail").sum()

    print("Students passed:", passed_count)
    print("Students failed:", failed_count)

    print("\n3. SUBJECT-WISE AVERAGES")
    print("-" * 35)

    for subject in SUBJECTS:
        print(f"{subject}: {df[subject].mean():.2f}")

    print("\n4. TOP 5 PERFORMERS")
    print("-" * 35)

    top_students = df.nlargest(5, "Average")

    print(
        top_students[
            ["Student_ID", "Name", "Average", "Grade"]
        ].round(2).to_string(index=False)
    )

    print("\n5. DEPARTMENT-WISE AVERAGES")
    print("-" * 35)

    department_averages = df.groupby("Department")["Average"].mean()

    print(department_averages.round(2).to_string())


def save_results(df):
    """Save analysis results into CSV reports."""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_DIR / "student_results.csv", index=False)

    subject_summary = pd.DataFrame({
        "Subject": SUBJECTS,
        "Average_Marks": [
            df[subject].mean() for subject in SUBJECTS
        ]
    })

    subject_summary.to_csv(
        OUTPUT_DIR / "subject_summary.csv",
        index=False
    )

    print("\nReports saved successfully.")
    print("Output folder:", OUTPUT_DIR.resolve())


def main():
    try:
        students = load_data()
        results = calculate_results(students)

        show_analysis(results)
        save_results(results)

        print("\nProject executed successfully!")

    except (OSError, ValueError, KeyError) as error:
        print("\nERROR:", error)


if __name__ == "__main__":
    main()