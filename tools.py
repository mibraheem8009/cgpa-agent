from pathlib import Path

COURSES = {
1: [("MS-251", "Probability & Statistics", 3.0),
("GE-160", "Applications of ICT", 3.0),
("GE-169", "Applied Physics", 3.0),
("GE-167", "Discrete Structures", 3.0),
("HQ-001", "Quran Translation - I", 0.5),
("GE-190", "Functional English", 3.0)],
2: [("CC-112", "Programming Fundamentals", 3.0),
("CC-112-L", "Programming Fundamentals Lab", 1.0),
("CC-110", "Digital Logic Design", 2.0),
("CC-110-L", "Digital Logic Design Lab", 1.0),
("MS-252", "Linear Algebra", 3.0),
("GE-191", "Expository Writing", 3.0),
("GE-163", "Islamic Studies", 2.0),
("HQ-002", "Quran Translation - II", 0.5)],
3: [("CC-211", "Object Oriented Programming", 3.0),
("CC-211-L", "Object Oriented Programming Lab", 1.0),
("CC-215", "Database Systems", 3.0),
("CC-215-L", "Database Systems Lab", 1.0),
("CC-210", "Computer Organization & Assembly Language", 3.0),
("GE-162", "Calculus & Analytical Geometry", 3.0),
("GE-192", "Introduction to Management", 2.0),
("HQ-003", "Quran Translation - III", 0.5)],
4: [("CC-213", "Data Structures", 3.0),
("CC-213-L", "Data Structures Lab", 1.0),
("CC-312", "Information Security", 3.0),
("CC-214", "Computer Networks", 3.0),
("CC-212", "Software Engineering", 3.0),
("DC-220", "Advanced Database Management Systems", 3.0),
("HQ-004", "Quran Translation - IV", 0.5)],
5: [("CC-313", "Analysis of Algorithms", 3.0),
("CC-310", "Artificial Intelligence", 3.0),
("DC-320", "Theory of Automata and Formal Languages", 3.0),
("DC-321", "Human Computer Interaction", 3.0),
("DC-322", "Computer Architecture", 3.0),
("EC-330", "Web Technologies / Elective", 3.0),
("HQ-005", "Quran Translation - V", 0.5)],
6: [("CC-311", "Operating Systems", 3.0),
("EC-333", "Mobile Application Development / Elective", 3.0),
("EC-324", "Software Construction & Development / Elective", 3.0),
("EC-335", "Machine Learning / Elective", 3.0),
("EC-334", "Game Design and Development / Elective", 3.0),
("MS-253", "Multivariable Calculus", 3.0),
("HQ-006", "Quran Translation - VI", 0.5)],
7: [("CC-411", "Final Year Project - I", 2.0),
("DC-328", "Parallel & Distributed Computing", 3.0),
("EC-345", "Computer Vision / Elective", 3.0),
("EC-425", "Software Quality Engineering / Elective", 3.0),
("MS-254", "Technical and Business Writing", 3.0),
("GE-263", "Entrepreneurship", 2.0),
("GE-262", "Professional Practices", 2.0),
("HQ-007", "Quran Translation - VII", 0.5)],
8: [("CC-412", "Final Year Project - II", 4.0),
("DC-421", "Compiler Construction", 3.0),
("UE-272", "Introduction to Marketing", 3.0),
("GE-168", "Ideology and Constitution of Pakistan", 2.0),
("GE-363", "Civics and Community Engagement", 2.0),
("HQ-008", "Quran Translation - VIII", 0.5)],
}

def marks_to_grade_points(marks: int) -> float | str:
    """ Use when a student gives marks (0-100) for a course and you need the grade point before computing any GPA """
    if type(marks) is not int:
        return "Error: marks must be an integer."

    if marks < 0 or marks > 100:
        return "Error: marks must be in between 0 and 100."

    if marks >= 85:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 61:
        return 2.3
    elif marks >= 58:
        return 2.0
    elif marks >= 55:
        return 1.7
    elif marks >= 50:
        return 1.0
    else:
        return 0.0


def calculate_semester_gpa( grade_points: list[float], credit_hours: list[float]) -> float | str:
    """Use when calculating semester GPA from course grade points and credit hours for every course. if marks are given instead of grade points, use the marks_to_grade_points tool first to calculate grade points."""

    if not grade_points or not credit_hours:
        return "Error: you must provide both grade points and credit hours."

    if len(grade_points) != len(credit_hours):
        return "Error: each grade point must have matching credit hours."

    total_points = 0.0
    total_credits = 0.0

    for gp, ch in zip(grade_points, credit_hours):
        if type(gp) not in (int, float) or not 0 <= gp <= 4:
            return "Error: grade points must be numbers between 0 and 4."

        if type(ch) not in (int, float) or not 0 < ch < float("inf"):
            return "Error: credit hours must be positive finite numbers."

        total_points += gp * ch
        total_credits += ch

    return total_points / total_credits


def calculate_new_cgpa(  current_cgpa: float, completed_credit_hours: float,  semester_gpa: float,  semester_credit_hours: float) -> float | str:
    """Use when a student wants to predict their CGPA after a semester. Needs current CGPA, completed credit hours, and the semester GPA with its credit hours, ask for any that are missing."""

    values = [
        current_cgpa,
        completed_credit_hours,
        semester_gpa,
        semester_credit_hours
    ]

    for value in values:
        if type(value) not in (int, float):
            return "Error: all inputs must be numbers."

    if not (0 <= current_cgpa <= 4 and 0 <= semester_gpa <= 4):
        return "Error: GPA and CGPA must be between 0 and 4."

    if not (0 <= completed_credit_hours < float("inf")):
        return "Error: completed credit hours must be finite and non-negative."

    if not (0 < semester_credit_hours < float("inf")):
        return "Error: semester credit hours must be finite and positive."

    previous_points = current_cgpa * completed_credit_hours
    semester_points = semester_gpa * semester_credit_hours
    total_hours = completed_credit_hours + semester_credit_hours

    return (previous_points + semester_points) / total_hours


def required_gpa_for_target(
    target_cgpa: float,
    current_cgpa: float,
    completed_credit_hours: float,
    remaining_credit_hours: float
) -> float | str:
    """Use when a student asks what future GPA is needed to reach a target CGPA.Get remaining_credit_hours using the get_remaining_credit_hours tool. """

    values = [
        target_cgpa,
        current_cgpa,
        completed_credit_hours,
        remaining_credit_hours
    ]

    for value in values:
        if type(value) not in (int, float):
            return "Error: all inputs must be numbers."

    if not 0 <= target_cgpa <= 4:
        return "Error: target CGPA must be between 0 and 4."

    if not 0 <= current_cgpa <= 4:
        return "Error: current CGPA must be between 0 and 4."

    if not 0 <= completed_credit_hours < float("inf"):
        return "Error: completed credit hours must be finite and non-negative."

    if not 0 < remaining_credit_hours < float("inf"):
        return "Error: remaining credit hours must be finite and positive."

    total_credits = completed_credit_hours + remaining_credit_hours
    target_points = target_cgpa * total_credits
    previous_points = current_cgpa * completed_credit_hours

    return (target_points - previous_points) / remaining_credit_hours


def get_semester_courses(semester: int) -> str:
    """Use when a student needs the course list and credit hours for a specific semester (1-8)."""

    if type(semester) is not int:
        return "Error: semester must be an integer."

    if semester < 1 or semester > 8:
        return "Error: semester must be between 1 and 8."

    result = ""

    for code, name, credit_hours in COURSES[semester]:
        result += f"{code}: {name} — {credit_hours} credit hours\n"

    return result

def get_remaining_credit_hours(current_semester: int) -> float | str:
    """ Use when a student wants to know how many credit hours remain in their degree after the current semester or Use when planning a target CGPA to determine total graded credit hours remaining after a given semester """

    if type(current_semester) is not int:
        return "Error: semester must be an integer."

    if current_semester < 1 or current_semester > 8:
        return "Error: semester must be between 1 and 8."

    total = 0.0

    for semester in range(current_semester + 1, 9):
        for code, name, credit_hours in COURSES[semester]:
            total += credit_hours

    return total


def save_report(filename: str, content: str) -> str:
    """Use only after producing a result worth keeping,Use only when the user requests saving a GPA result or plan."""

    if type(filename) is not str or not filename.strip():
        return "Error: filename must be a non-empty string."

    if type(content) is not str or not content.strip():
        return "Error: content must be non-empty text."

    filename = filename.strip()
    if Path(filename).name != filename or filename in {".", ".."}:
        return "Error: enter a filename without a folder path."

    if not filename.endswith(".txt"):
        filename += ".txt"

    reports_dir = Path(__file__).resolve().parent / "reports"

    try:
        reports_dir.mkdir(exist_ok=True)
        with (reports_dir / filename).open("x", encoding="utf-8") as f:
            f.write(content)
    except FileExistsError:
        return "Error: a report with that name already exists. Choose another name."
    except (OSError, ValueError):
        return "Error: could not save the report."

    return f"Report saved as {filename} on the server."