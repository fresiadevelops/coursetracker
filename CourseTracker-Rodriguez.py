# Dictionaries to store the data
# Dictionary Number 1-room numbers
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}
# Dictionary Number 2-instructors
instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}
# Dictionary Number 3-meeting times
meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Prompting user for a course #
course_number = input("Enter a course number (e.g., CSC101): ")

# Retrieving course details
if course_number in room_numbers:
    print(f"Course Number: {course_number}")
    print(f"Room Number: {room_numbers[course_number]}")
    print(f"Instructor: {instructors[course_number]}")
    print(f"Meeting Time: {meeting_times[course_number]}")
else:
    print("Course not found. Please check the course number and try again.")
