# Name: Ben Mickens
# Due Date: 11-09-2025
# Description: A Course Planner program that allows a student to add courses to a list, display the schedule, remove a course if needed, and view the final count.

print("--- Welcome to the Student Course Planner ---")

schedule = []

# Prompt user to enter courses
print("\nPlease enter 3 courses.")

# Use loop to get 3 courses
for i in range(3):
    course_name = input(f"Enter course name #{i + 1}: ")
    schedule.append(course_name)  # Adds the new course to the list

# Display the Schedule
print("\n--- Current Schedule ---")
print(schedule)

# Prompt user to drop a course
drop_response = input("\nWould you like to drop a course? (Y/N): ")

if drop_response.lower() == "y":
    course_to_drop = input("Enter the name of the course to remove: ")

    # Check if the course exists
    if course_to_drop in schedule:
        schedule.remove(course_to_drop)  # Remove the course
        print(f"Successfully removed: {course_to_drop}")
    else:
        print(f"Error: '{course_to_drop}' was not found in your schedule.")

# Display final results
print("\n--- Final Schedule Summary ---")
print(f"Your final list of courses: {schedule}")

# Use len() to count the remaining items in the list
print(f"Total courses remaining: {len(schedule)}")
