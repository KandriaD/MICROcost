#course information for all classes Spring 2025

# courseinfo.py

class Course:
    def __init__(self, name, sections, students, groups, rooms):
        self.name = name
        self.sections = sections
        self.students = students
        self.groups = groups
        self.rooms = rooms
        self.tables = len(rooms) * 6  # Each room has 6 tables

    def __repr__(self):
        return f"Course({self.name}, {self.sections}, {self.students}, {self.groups}, {self.rooms}, {self.tables} tables)"

# Creating course instances
micro140L = Course("MICRO140L", 2, 33, 16, ["115C", "114"])
micro351L = Course("MICRO351L", 2, 31, 15, ["115B", "115B"]) #updated on 5/5 for summer session 2 2025
micro401L = Course("MICRO401L", 2, 34, 17, ["115C", "115B"])
micro461L = Course("MICRO461L", 1, 15, 7, ["113"])
micro463L = Course("MICRO463L", 1, 15, 7, ["115B"])

# Storing all courses in a dictionary for easy access
courses = {
    micro140L.name: micro140L,
    micro351L.name: micro351L,
    micro401L.name: micro401L,
    micro461L.name: micro461L,
    micro463L.name: micro463L
}
