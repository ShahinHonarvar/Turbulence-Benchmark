
def remove_repeat_chars(s):
    # Create a set to keep track of the characters we've seen
    seen = set()

    # Loop through each character in the string
    for char in s:
        if char not in seen:
            # If the character is not in the set, add it and move on
            seen.add(char)

        else:
            # If the character is already in the set, remove all occurrences of that character from the string
            new_s = s.replace(char, '')
            return new_s
