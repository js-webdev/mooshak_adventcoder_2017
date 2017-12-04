"""Weekdays in December"""
import sys
import datetime

def get_weekday(number):
    return datetime.date(2017, 12, number).weekday()

for input in sys.stdin.readlines():
    values = input.split(' ')
    for i, value in enumerate(values):
        if value == "end":
            sys.exit(0)
        elif value == "December":
            if value[i+1] != "end":
                if int(values[i+1]) <= 31 and int(values[i+1]) >= 1:
                    weekdays = ["Monday",
                                "Tuesday",
                                "Wednesday",
                                "Thursday",
                                "Friday",
                                "Saturday",
                                "Sunday"]
                    sys.stdout.write(weekdays[get_weekday(int(values[i+1]))]+"\n")
