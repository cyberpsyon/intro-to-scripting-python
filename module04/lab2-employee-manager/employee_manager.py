# Author: Ben Mickens
# Due Date: 11-16-2025
# Function: The program implements the employee class

import employee_manager_utils as em

def main():
    # Create list of employees
    employees = [
        em.Employee("Splinter", "Human Resources", 100000, 10),
        em.Employee("Michelangelo", "Food & Beverage", 85000, 7),
        em.Employee("Raphael", "Customer Service", 90000, 7),
        em.Employee("Leonardo", "Project Management", 95000, 9),
        em.Employee("Donatello", "Information Technology", 90000, 8)
    ]
    # Output current employee information
    print("\n--- Current Employee Information ---")
    for employee in employees:
        employee.display_info()

    # Show employees with high-performance >= 8
    print("\n--- High-performance Employees (Score >= 8) ---")
    for employee in employees:
        if employee.performance_score >= 8:
            print(f"{employee.name} (Score: {employee.performance_score})")

    # Apply 5% raise
    print("\n--- Applying 5% raise to Top Talent (Score >= 9) ---")
    for employee in employees:
        if employee.performance_score >= 9:
            employee.apply_raise(5)
            print(f"Raise applied for {employee.name}")

    # Output updated salary information
    print("\n--- Updated Salary Information ---")
    for employee in employees:
        print(f"{employee.name} : {employee.get_formatted_salary()}")

if __name__ == "__main__":
    main()


