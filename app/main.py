import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: list[Group]) -> int:
    if not groups:
        with open("groups.pickle", "wb") as f:
            pickle.dump(groups, f)
        return 0  # Return 0 if there are no groups
    else:
        with open("groups.pickle", "wb") as f:
            pickle.dump(groups, f)
        max_students = max(len(group.students) for group in groups)
        return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list[str]:
    specialties = set()
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        for group in groups:
            specialties.add(group.specialty.name)
    return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
