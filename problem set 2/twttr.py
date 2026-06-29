def main():
    # Prompt user for input
    text = input("Input: ")
    
    # Initialize an empty string for the output
    output = ""
    
    # Iterate through each character in the input
    for char in text:
        # Check if the character is a vowel (uppercase or lowercase)
        if char.lower() not in ['a', 'e', 'i', 'o', 'u']:
            # If not a vowel, add it to the output
            output += char
    
    # Print the result
    print(f"Output: {output}")

if __name__ == "__main__":
    main()