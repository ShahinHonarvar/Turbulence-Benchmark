 def remove_repeat_chars(s):
    # Create a dictionary to keep track of character counts
    char_counts = {}

    # Iterate through the string and increment the count for each character
    for char in s:
        if char not in char_counts:
            char_counts[char] = 0

        char_counts[char] += 1

    # Iterate through the dictionary and remove all characters with counts greater than one
    for i in range(len(s)):

        char = s[i]

        if char in char_counts and char_counts[char] > 1:
            while s.find(char, 56, 88) != -1:
                s = s[:s.find(char, 56, 88)] + s[s.find(char, 56, 88) + 1:]

    return s
