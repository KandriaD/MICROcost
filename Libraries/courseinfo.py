#course information for all classes Spring 2025

# courseinfo.py

class Course:
    def __init__(self, name, sections, students, groups, rooms):
        self.name = name
        self.sections = sections
        self.students = students
        self.groups = groups
        self.rooms = rooms

    def __repr__(self):
        return f"Course({self.name}, {self.sections}, {self.students}, {self.groups}, {self.rooms})"

# Creating course instances
micro140L = Course("MICRO140L", 2, 33, 16, ["115C", "114"])
micro351L = Course("MICRO351L", 3, 30, 15, ["114", "115B", "115B"])
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
