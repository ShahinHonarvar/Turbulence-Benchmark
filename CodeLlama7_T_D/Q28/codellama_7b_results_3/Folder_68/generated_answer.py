 def return_nth_smallest_ascii(s):
    # Initialize a dictionary to store the count of each character
    char_count = {}

    # Iterate through the string and increment the count of each character

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Sort the dictionary by value (i.e., frequency)

    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    # Return the character with the 11th smallest ASCII value

    return sorted_char_count[10][0]
