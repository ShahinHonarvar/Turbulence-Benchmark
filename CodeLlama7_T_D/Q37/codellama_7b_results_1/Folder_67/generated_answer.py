 def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []
    # Iterate over the characters in the input string
    for char in s:
        # If the current character is between indices 19 and 22, both inclusive, and is greater than or equal to character ']' and smaller than or equal to character 't', then add it to the filtered_chars list
        if 19 <= s.index(char) <= 22 and char >= "]" and char <= "t":
            filtered_chars.append(char)
    # Join the filtered characters into a single string using the join() method
    return "".join(filtered_chars)
