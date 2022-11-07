import time
from application.salary import print_status_salary
from application.db.people import print_status_people

if __name__ == "__main__":
    print(time.strftime("%d.%m.%y-%H:%M"))
    print_status_salary()
    print_status_people()