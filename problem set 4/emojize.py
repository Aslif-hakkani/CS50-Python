import emoji


def main():
    # Get user input
    user_input = input("Input: ")

    # Emojize the input (support both codes and short aliases like :thumbsup:)
    emojized_text = emoji.emojize(user_input, language="alias")

    # Output the result with the required "Output: " prefix
    print(f"Output: {emojized_text}")


if __name__ == "__main__":
    main()
