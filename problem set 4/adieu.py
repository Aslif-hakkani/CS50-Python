def main():
    names = []

    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break

    print(f"\nAdieu, adieu, to {join_names(names)}")


def join_names(names):
    if len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f"{names[0]} and {names[1]}"
    else:
        return ", ".join(names[:-1]) + f", and {names[-1]}"


if __name__ == "__main__":
    main()
