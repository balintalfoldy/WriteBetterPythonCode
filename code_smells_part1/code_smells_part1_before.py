"""
Very advanced Employee management system.
"""

from dataclasses import dataclass
from typing import List

# The fixed nr of vacation days that can be paid out.
FIXED_VACATION_DAYS_PAYOUT = 5


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    #! Role str is too borad, use Enum for correct values
    name: str
    role: str
    vacation_days: int = 25

    #! Using boolean flags to make a method do 2 different things
    #! Split this function into two
    def take_a_holiday(self, payout: bool) -> None:
        """Let the employee take a single holiday, or pay out 5 holidays."""
        if payout:
            #! Use custom error types
            # check that there are enough vacation days left for a payout
            if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
                raise ValueError("You don't have enough holidays left over for a payout.\
                        Remaining holidays.")

            #! Remove the exception if you don't do anythin with it
            try:
                self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
                print(
                    f"Paying out a holiday. Holidays left: {self.vacation_days}")
            except Exception:
                # this should never happen
                pass
        else:
            if self.vacation_days < 1:
                raise ValueError(
                    "You don't have any holidays left. Now back to work, you!"
                )
            self.vacation_days -= 1
            print("Have fun on your holiday. Don't forget to check your emails!")


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    hourly_rate: float = 50
    #! Vague identifiers
    amount: int = 10


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 5000


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        self.employees.append(employee)

    #! duplicates - the only thing changing is the role, replace it
    #! with a generic method
    def find_managers(self) -> List[Employee]:
        """Find all manager employees."""
        managers = []
        #! replace it with list comprehension
        for employee in self.employees:
            if employee.role == "manager":
                managers.append(employee)
        return managers

    def find_vice_presidents(self) -> List[Employee]:
        """Find all vice-president employees."""
        vice_presidents = []
        for employee in self.employees:
            if employee.role == "vice_president":
                vice_presidents.append(employee)
        return vice_presidents

    def find_interns(self) -> List[Employee]:
        """Find all interns."""
        interns = []
        for employee in self.employees:
            if employee.role == "intern":
                interns.append(employee)
        return interns

    #! Using isinstance -> bad practice -> introduces direct dependency
    #! between Company and Employee subclasses, also whenever you add new employee
    #! type you need to extend the if statements
    #! Solve this by removing pay_employee and add a pay method to each employee type
    def pay_employee(self, employee: Employee) -> None:
        """Pay an employee."""
        if isinstance(employee, SalariedEmployee):
            print(
                f"Paying employee {employee.name} a monthly salary of ${employee.monthly_salary}."
            )
        elif isinstance(employee, HourlyEmployee):
            print(
                f"Paying employee {employee.name} a hourly rate of \
                ${employee.hourly_rate} for {employee.amount} hours."
            )


def main() -> None:
    """Main function."""

    company = Company()

    company.add_employee(SalariedEmployee(name="Louis", role="manager"))
    company.add_employee(HourlyEmployee(name="Brenda", role="president"))
    company.add_employee(HourlyEmployee(name="Tim", role="intern"))

    print(company.find_vice_presidents())
    print(company.find_managers())
    print(company.find_interns())
    company.pay_employee(company.employees[0])
    company.employees[0].take_a_holiday(False)


if __name__ == "__main__":
    main()
