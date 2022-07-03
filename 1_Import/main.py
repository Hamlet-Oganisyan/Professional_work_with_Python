from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

dt = datetime.now()

def main():
    print('Сегодня: ', dt)
    calculate_salary()
    get_employees()


if __name__ == '__main__':
    main()