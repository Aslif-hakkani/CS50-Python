import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)

    if not match:
        return False

    parts = match.groups()

    for part in parts:
        if len(part) > 1 and part.startswith("0"):
            return False

        if int(part) > 255:
            return False

    return True


if __name__ == "__main__":
    main()
