
import re
from pathlib import Path

import pandas as pd
import streamlit as st

from main import calculate_results, SUBJECTS

DATA_FILE = Path(__file__).parent / "students.csv"
REQUIRED_COLUMNS = [
    "Student_ID", "Name", "Department",
    *SUBJECTS, "Attendance"
]

st.set_page_config(
    page_title="Student Analytics AI",
    page_icon="📊",
    layout="wide",
)

st.title("🎓 Student Analytics AI")
st.caption("Ask questions about student data, explore performance, and add records.")

# ---------- Data functions ----------

def read_students():
    df = pd.read_csv(DATA_FILE)

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing CSV columns: {missing}")

    if df["Student_ID"].duplicated().any():
        raise ValueError("The CSV contains duplicate student IDs.")

    for col in SUBJECTS + ["Attendance"]:
        df[col] = pd.to_numeric(df[col], errors="raise")
        if not df[col].between(0, 100).all():
            raise ValueError(f"{col} values must be between 0 and 100.")

    return df[REQUIRED_COLUMNS]


def find_student(df, query):
    query = query.strip()
    return df[
        df["Student_ID"].astype(str).str.lower().eq(query.lower())
        | df["Name"].astype(str).str.contains(
            re.escape(query), case=False, na=False
        )
    ]


def interpret_question(question, df):
    q = question.lower().strip()
    results = calculate_results(df)

    if any(word in q for word in ["all students", "show students", "list students"]):
        return "Here are the current student records.", results

    if "top" in q or "highest performer" in q or "best students" in q:
        match = re.search(r"top\s+(\d+)", q)
        count = min(int(match.group(1)), 50) if match else 5
        subset = results

        department = re.search(r"\b(?:in|from)\s+([a-z]+)\b", q)
        if department and department.group(1).upper() in (
            df["Department"].astype(str).str.upper().unique()
        ):
            subset = results[
                results["Department"].str.lower() == department.group(1).lower()
            ]

        return f"Top {count} students ranked by average marks:", (
            subset.nlargest(count, "Average")
        )

    if any(word in q for word in ["failed", "fail students", "who failed"]):
        return "Students who failed at least one subject:", results[
            results["Result"] == "Fail"
        ]

    if "subject" in q and any(word in q for word in ["average", "analysis", "marks"]):
        summary = pd.DataFrame({
            "Subject": SUBJECTS,
            "Average Marks": [df[s].mean() for s in SUBJECTS],
        })
        return "Average marks by subject:", summary.round(2)

    if "department" in q and any(word in q for word in ["average", "compare", "performance"]):
        summary = results.groupby("Department", as_index=False)["Average"].mean()
        summary["Average"] = summary["Average"].round(2)
        return "Average performance by department:", summary

    if "class average" in q or "overall average" in q:
        return (
            f"The class average is {results['Average'].mean():.2f} marks.",
            None,
        )

    if "attendance" in q and any(word in q for word in ["low", "below", "less"]):
        match = re.search(r"(\d+(?:\.\d+)?)", q)
        limit = float(match.group(1)) if match else 75
        return f"Students with attendance below {limit:g}%:", df[
            df["Attendance"] < limit
        ]

    if q.startswith("find ") or q.startswith("search "):
        term = re.sub(r"^(find|search)\s+(student\s+)?", "", question, flags=re.I)
        matches = find_student(results, term)
        if matches.empty:
            return f"No student found matching '{term}'.", None
        return "Matching student records:", matches

    return (
        "I couldn't identify that request yet. Try asking for the top 5 students, "
        "failed students, class average, subject averages, department comparison, "
        "attendance below 75%, or 'find S004'.",
        None,
    )


def validate_new_student(values, df):
    values = {k: str(v).strip() for k, v in values.items()}

    if any(not value for value in values.values()):
        raise ValueError("Every field is required.")

    if df["Student_ID"].astype(str).str.lower().eq(
        values["Student_ID"].lower()
    ).any():
        raise ValueError("That Student ID already exists.")

    for col in SUBJECTS + ["Attendance"]:
        try:
            score = float(values[col])
        except ValueError:
            raise ValueError(f"{col} must be a number.")

        if not 0 <= score <= 100:
            raise ValueError(f"{col} must be between 0 and 100.")

        values[col] = score

    return values


def append_student(values):
    # Re-read immediately before writing to avoid relying on stale page data.
    current = read_students()
    values = validate_new_student(values, current)

    new_row = pd.DataFrame([values], columns=REQUIRED_COLUMNS)
    updated = pd.concat([current, new_row], ignore_index=True)
    updated.to_csv(DATA_FILE, index=False)


# ---------- Load data ----------

try:
    students = read_students()
    results = calculate_results(students)
except Exception as exc:
    st.error(f"Could not load the dataset: {exc}")
    st.stop()

# ---------- Dashboard ----------

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Students", len(results))
c2.metric("Class Average", f"{results['Average'].mean():.2f}")
c3.metric("Passed", int((results["Result"] == "Pass").sum()))
c4.metric("Failed", int((results["Result"] == "Fail").sum()))

tab_chat, tab_students, tab_add = st.tabs(
    ["💬 Ask Assistant", "📋 Student Records", "➕ Add Student"]
)

with tab_chat:
    st.subheader("Ask your data assistant")
    st.caption("The assistant reads the current CSV. It supports the requests listed below.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            if message.get("data") is not None:
                st.dataframe(message["data"], use_container_width=True)

    question = st.chat_input("Ask about student performance...")

    if question:
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        answer, data = interpret_question(question, students)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer,
            "data": data,
        })
        st.rerun()

    st.markdown("**Examples**")
    st.markdown(
        "- `Show the top 5 students`\n"
        "- `Find S004`\n"
        "- `Show failed students`\n"
        "- `What is the class average?`\n"
        "- `Compare department performance`\n"
        "- `Show attendance below 75%`"
    )

with tab_students:
    st.subheader("Student Records")
    search = st.text_input("Search by student name or ID")
    view = results.copy()

    if search.strip():
        view = find_student(view, search)

    st.dataframe(view, use_container_width=True, hide_index=True)

    st.download_button(
        "Download current student results",
        data=results.to_csv(index=False).encode("utf-8"),
        file_name="student_results.csv",
        mime="text/csv",
    )

with tab_add:
    st.subheader("Add a student")
    st.write("Complete the form. The CSV will only be updated after confirmation.")

    with st.form("add_student_form"):
        student_id = st.text_input("Student ID", placeholder="S021")
        name = st.text_input("Student name")
        department = st.selectbox(
            "Department",
            sorted(students["Department"].dropna().unique().tolist()),
        )

        marks = {}
        mark_cols = st.columns(2)
        for i, subject in enumerate(SUBJECTS):
            with mark_cols[i % 2]:
                marks[subject] = st.number_input(
                    subject, min_value=0.0, max_value=100.0, value=50.0
                )

        attendance = st.number_input(
            "Attendance (%)", min_value=0.0, max_value=100.0, value=75.0
        )

        confirm = st.checkbox("I have checked the details and want to save this record.")
        submitted = st.form_submit_button("Validate and save student")

    if submitted:
        if not confirm:
            st.warning("Please confirm the record before saving.")
        else:
            new_record = {
                "Student_ID": student_id,
                "Name": name,
                "Department": department,
                **marks,
                "Attendance": attendance,
            }
            try:
                append_student(new_record)
                st.success(f"Student {student_id} saved to students.csv.")
                st.rerun()
            except (ValueError, OSError, pd.errors.ParserError) as exc:
                st.error(f"Record was not saved: {exc}")
