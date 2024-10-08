import datetime

def is_today_over_x_date(date_to_compare):
    today = datetime.date.today()
    # Extract year, month, and day from the string
    day, month, year = map(int, date_to_compare.split("/"))
    target_date = datetime.date(year, month, day)

    if today > target_date:
        # print("Today:", today, "is over:", target_date)
        return True
    else:
        # print("Today:", today, "is NOT over:", target_date)
        return False
