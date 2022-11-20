from datetime import datetime, timedelta

#тест проводился от 21.11.22
test_users = [
    {"name": "Sergey", "birthday": datetime(year=1992, month=11, day=23)},  #не показывает
    {"name": "Alexey", "birthday": datetime(year=1992, month=12, day=4)},   #не показывает
    {"name": "Sasha", "birthday": datetime(year=1992, month=11, day=28)},   #ПН
    {"name": "Nastya", "birthday": datetime(year=1992, month=12, day=3)},   #не показывает
    {"name": "Olena", "birthday": datetime(year=1992, month=12, day=3)},    #не показывает
    {"name": "Vasya", "birthday": datetime(year=1992, month=12, day=2)},    #ПТ
    {"name": "Roma", "birthday": datetime(year=1992, month=12, day=2)},     #ПТ
    {"name": "Stas", "birthday": datetime(year=1992, month=12, day=1)},     #ЧТ
    {"name": "Vitos", "birthday": datetime(year=1992, month=11, day=30)},   #СР
    {"name": "Vladimir", "birthday": datetime(year=1992, month=11, day=29)},#ВТ
    {"name": "Masha", "birthday": datetime(year=1992, month=11, day=28)},   #ПН
    {"name": "Natasha", "birthday": datetime(year=1992, month=12, day=15)}  #не показывает
]

week_bday = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": []
}

def week_control(bday, current_datetime):
    diff_day = 5 - abs(current_datetime.weekday())
    next_week_Sat = current_datetime + timedelta(days=diff_day)
    diff_next_week = (bday - next_week_Sat).days
    if 0 <= diff_next_week <= 2:
        return("Monday")
    elif diff_next_week == 3:
        return("Tuesday")
    elif diff_next_week == 4:
        return("Wednesday")
    elif diff_next_week == 5:
        return("Thursday")    
    elif diff_next_week == 6:
        return("Friday")
    else:
        return("No result")    

def print_user_list(week_bday):
    for key, value in week_bday.items():
        if value:
            print(f"{key}: {', '.join(value)}")

def get_birthdays_per_week(users: list):
    current_datetime = datetime.now()
    for name in users:
        bday = name["birthday"]
        bday_this_year = datetime(year=current_datetime.year, month=bday.month, day=bday.day)                  
        day_bday = week_control(bday_this_year, current_datetime)
        if day_bday == "No result":
            continue
        (week_bday[day_bday]).append(name["name"])
    print_user_list(week_bday)

if __name__ == "__main__":
    get_birthdays_per_week(test_users)