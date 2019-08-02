employees = []
running = True


class Employees:

    def __init__(self, n, d, p, r):
        self.n = n
        self.d = d
        self.p = p
        self.r = r

    def compute(self, h):
        return h * self.r


while running:
    print("Choose your option: ")
    print("[1] Add new employee")
    print("[2] Enter hourly of employee")
    print("[3] Show employee information")
    print("[4] Exit", "\n")

    print("Enter option: ", end="")
    ans = int(input())

    if ans == 1:
        print("Enter employee name: ", end="")
        n = (input())

        print("Enter department: ", end="")
        d = input()

        print("Enter position: ", end="")
        p = input()

        print("Enter rate: ", end="")
        r = int(input())

        employees.append(Employees(n, d, p, r))

        continue

    elif ans == 2:
        e1 = Employees(n, d, p, r)
        print("Enter the index of the employee: ", end="")

        y = int(input())
        print(employees[y].n, " is selected")
        print("Enter the hourly of employee: ", end="")
        z = int(input())
        print(employees[y].r * z)
        continue

    elif ans == 3:

        for x in employees:
            print("\nName:", x.n, "\nDepartment:", x.d, "\nPosition:", x.p, "\nRate:", x.r,"\n")

        continue

    elif ans == 4:
        running = False

    else:
        print("Invalid input, please try again: ")
        continue
    break
