#course information for all classes Spring 2025

# courseinfo.py

class Course:
    def __init__(self, name, sections, students, groups, rooms):
        self.name = name
        self.sections = sections
        self.students = students
        self.groups = groups
        self.rooms = rooms
        self.tables = sum(5 if room == "113" else 6 for room in rooms)

    def __repr__(self):
        return f"Course({self.name}, {self.sections}, {self.students}, {self.groups}, {self.rooms}, {self.tables} tables)"

# Creating course instances
micro140L = Course("MICRO140L", 2, 33, 16, ["115C", "114"])
micro351L = Course("MICRO351L", 2, 31, 15, ["115B", "115B"]) #updated on 5/5 for summer session 2 2025
micro401L = Course("MICRO401L", 2, 34, 17, ["115C", "115B"])
micro461L = Course("MICRO461L", 2, 28, 10, ["113", "114"])
micro463L = Course("MICRO463L", 1, 15, 7, ["115B"])
micro475L = Course("MICRO475L", 1, 19, 6, ["115C"])

# Storing all courses in a dictionary for easy access
courses = {
    micro140L.name: micro140L,
    micro351L.name: micro351L,
    micro401L.name: micro401L,
    micro461L.name: micro461L,
    micro463L.name: micro463L,
    micro475L.name: micro475L
}
