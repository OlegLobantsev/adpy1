import datetime
from application.salary import *
from application.db.people import *

dt = datetime.datetime.now()


def day():
    return str(dt.strftime("in %A, %d %B %Y "))


if __name__ == '__main__':
    print(get_employees(), day())
    print(calculate_salary(), day())
