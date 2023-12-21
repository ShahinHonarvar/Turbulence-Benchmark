
def remove_repeat_chars(s):
    # Create a dictionary to store the counts of each character
    char_counts = {}

    # Iterate over the characters in the string
    for char in s:

        # If the character is already in the dictionary, increment its count
        if char in char_counts:
            char_counts[char] += 1

        # Otherwise, add the character to the dictionary and set its count to 1
        else:
            char_counts[char] = 1

    # Iterate over the characters in the string again
    for i in range(len(s)):

        # If the current character is not in the dictionary, or if it is but its count is 1, remove all occurrences of that character from the string and continue to the next character
        if s[i] not in char_counts or char_counts[s[i]] == 1:
            new_string = ""
            for j in range(len(s)):
                if j != i or s[j] != s[i]:
                    new_string += s[j]

            return new_string

        # If the current character is in the dictionary and its count is greater than 1, decrement its count and continue to the next character
        else:
            char_counts[s[i]] -= 1
            continue

    # If all characters have a count of 1, return the original string
    else:
        return s
