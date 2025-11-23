# Author: Ben Mickens
# Due Date: 11-16-2025
# Function: The program contains the employee class

# Initialize employee class
class Employee:
    def __init__(self, name, department, salary, performance_score):
        self.name = name
        self.department = department
        self.salary = salary
        self.performance_score = performance_score

    # Override output of employee information
    def __str__(self):
        return f"{self.name} | {self.department} | {self.get_formatted_salary()} | {self.performance_score}"

    # Output information
    def display_info(self):
        print(self)

    # Apply raise to salary
    def apply_raise(self, percent):
        self.salary += self.salary * (percent / 100)

    # Format salary
    def get_formatted_salary(self):
        return f"${self.salary:,.2f}"
