from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):

    today = date.today()
    current_weekday = today.weekday()
    start_of_week = today - timedelta(days=current_weekday)
    end_of_next_week = start_of_week + timedelta(days=13)
    days_of_week = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}

    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        this_year_birthday = birthday.replace(year=today.year)

        if this_year_birthday < today:
            this_year_birthday = birthday.replace(year=today.year + 1)

        if start_of_week <= this_year_birthday <= end_of_next_week:
            birthday_weekday = this_year_birthday.weekday()

            if birthday_weekday >= 5:  # Субота або неділя
                days_of_week["Monday"].append(name)
            else:
                weekday_name = list(days_of_week.keys())[birthday_weekday]
                days_of_week[weekday_name].append(name)

    return {day: user_list for day, user_list in days_of_week.items() if user_list}


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Elon Musk", "birthday": datetime(1971, 6, 28).date()},
        {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        if names:
            print(f"{day_name}: {', '.join(names)}")
