def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length requirement (2-6 characters)
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Check that all characters are alphanumeric (no periods, spaces, punctuation)
    if not s.isalnum():
        return False
    
    # Check that first two characters are letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    
    # Check number placement rules
    number_started = False
    for i in range(len(s)):
        if s[i].isdigit():
            # First number cannot be '0'
            if not number_started and s[i] == '0':
                return False
            number_started = True
        elif number_started:
            # If we find a letter after a number has started, it's invalid
            return False
    
    return True

if __name__ == "__main__":
    main()