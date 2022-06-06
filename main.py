import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

dt = datetime.datetime.now()


def day():
    return str(dt.strftime("in %A, %d %B %Y "))


if __name__ == '__main__':
    print(get_employees(), day())
    print(calculate_salary(), day())
