
import calendar
# from copy import deepcopy
from datetime import datetime
from datetime import timedelta


_users = [
    {"name" : "Vova"        , "birthday" : datetime(1977,1,3)},
    {"name" : "Bob Junior"  , "birthday" : datetime(2020,12,31)},
    {"name" : "Alex"        , "birthday" : datetime(1999,6,19)},
    {"name" : "Anatoly"     , "birthday" : datetime(1969,12,10)},
    {"name" : "Misha"       , "birthday" : datetime(2017,6,10)},

    {"name" : "Mary"        , "birthday" : datetime(1953,2,14)},
    {"name" : "Tanya Junior", "birthday" : datetime(2022,2,15)},
    {"name" : "Tanya"       , "birthday" : datetime(1973,2,15)},
    {"name" : "Olga Junior" , "birthday" : datetime(2022,2,16)},
    {"name" : "Olga"        , "birthday" : datetime(1977,2,16)},
    {"name" : "Boris"       , "birthday" : datetime(1940,2,17)},

    {"name" : "Joe"         , "birthday" : datetime(2020,2,29)},
    {"name" : "Hloe"        , "birthday" : datetime(2019,2,28)},
]

# def is_leap(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def _replace_year(date: datetime,year: int) -> datetime:
    if date.month == 2 and date.day == 29 and not calendar.isleap(year):
        return datetime(year,date.month,28)
    else:
        return datetime(year,date.month,date.day)


def get_birthdays(users: list,date_from: datetime, date_to: datetime) -> dict:
    """Filter users' list by datetime"""

    result = []

    # Check period bounds
    if date_from > date_to:
        print("Error: start date must be lesser!!!")
        return result
    if calendar.isleap(date_from.year) and date_from.month < 3 or calendar.isleap(date_to.year) and date_to.month > 2:
        MAX_DAYS = 366
    else:
        MAX_DAYS = 365
    delta = date_to - date_from
    if delta.days > MAX_DAYS - 1:
        print("Error: Period is greater than year!!!")
        return result
    
    for user in users:
        new_date_from   = _replace_year(user["birthday"],date_from.year)
        new_date_to     = _replace_year(user["birthday"],date_to.year)
        if new_date_from >= date_from and new_date_from <= date_to:
            user["current_birthday"] = new_date_from
            result.append(user)
        elif new_date_to >= date_from and new_date_to <= date_to:
            user["current_birthday"] = new_date_to
            result.append(user)
        else:
            pass
    return result
    
    # it = filter(
    #     lambda user:
    #         (
    #             replace_year(user["birthday"],date_from.year)    >= date_from and
    #             replace_year(user["birthday"],date_from.year)    <= date_to
    #         ) or (
    #             replace_year(user["birthday"],date_to.year)      >= date_from and
    #             replace_year(user["birthday"],date_to.year)      <= date_to
    #         )
    #     ,
    #     users
    # )
    # return list(it)


def _print_birthdays(users_filtered: dict, sort = True) -> None:
    """ """
    # birthdays = {i: [] for i in range(7)}
    birthdays = {}

    if sort:
        users_filtered.sort(key = lambda user : user["birthday"])
    # Fill birthdays' dict
    for user in users_filtered:
        weekday = user["current_birthday"].weekday()
        weekday = 0 if weekday > 4 else weekday
        if weekday not in birthdays:
            birthdays[weekday] = []
        birthdays[weekday].append(user["name"])
    
    birthdays = dict(sorted(birthdays.items())) #sort by weekday number

    # Print
    for k,names in birthdays.items():
        if names:
            weekday = calendar.day_name[k]
            print(f"{weekday}:", ", ".join(names))

def get_birthdays_per_week(users: list, date: datetime = datetime.now()) -> dict:

    weekday = date.weekday()
    WORKWEEK_SIZE = 4
    diff = 0
    shift = 0
    if not weekday:
        diff = 0 # Start from Monday
        shift = WORKWEEK_SIZE
    else:
        diff = 5 - weekday # Shift start date to first Weekend
        shift = WORKWEEK_SIZE + 2
    
    date_from = date + timedelta(days = diff)
    date_to = date_from + timedelta(days = shift)

    # users.sort(key = lambda user : user["birthday"])
    users_filtered = get_birthdays(users,date_from,date_to)
    _print_birthdays(users_filtered)
    return

# result = get_birthdays(_users,datetime(2022,12,31),datetime(2023,12,31))
# result = get_birthdays(_users,datetime(2024,1,1),datetime(2025,1,1))
# get_birthdays_per_week(_users,datetime(2023,2,13))
# get_birthdays_per_week(_users)
# get_birthdays_per_week(_users,datetime.now() + timedelta(days=1))
# get_birthdays_per_week(_users,datetime.now())
# get_birthdays_per_week(_users,datetime.now() - timedelta(days=1))
# get_birthdays_per_week(_users,datetime.now() - timedelta(days=3))
# get_birthdays_per_week(_users,datetime.now() - timedelta(days=4))
