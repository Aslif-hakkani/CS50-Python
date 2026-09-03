import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)",
        s
    )

    if not match:
        raise ValueError

    hour1, minute1, period1, hour2, minute2, period2 = match.groups()

    hour1 = int(hour1)
    hour2 = int(hour2)
    minute1 = int(minute1) if minute1 else 0
    minute2 = int(minute2) if minute2 else 0

    if hour1 < 1 or hour1 > 12:
        raise ValueError

    if hour2 < 1 or hour2 > 12:
        raise ValueError

    if minute1 < 0 or minute1 > 59:
        raise ValueError

    if minute2 < 0 or minute2 > 59:
        raise ValueError

    if period1 == "AM" and hour1 == 12:
        hour1 = 0
    elif period1 == "PM" and hour1 != 12:
        hour1 += 12

    if period2 == "AM" and hour2 == 12:
        hour2 = 0
    elif period2 == "PM" and hour2 != 12:
        hour2 += 12

    return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"


if __name__ == "__main__":
    main()
