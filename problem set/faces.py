def convert(s):
    return s.replace(":)", "🙂").replace(":(", "🙁")


def main():
    print(convert(input()))


main()
