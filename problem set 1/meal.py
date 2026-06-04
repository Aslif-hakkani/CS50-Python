def main():
    time = input("What time is it? ")
    hours = convert(time)

    if 7.0 <= hours <= 8.0:
        print("breakfast time")  # Indented 4 spaces
    elif 12.0 <= hours <= 13.0:
        print("lunch time")       # Indented 4 spaces
    elif 18.0 <= hours <= 19.0:
        print("dinner time")      # Indented 4 spaces

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60

if __name__ == "__main__":
    main()