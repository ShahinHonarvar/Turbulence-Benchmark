 def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter (lowercase or uppercase)
        if char.isalpha():
            # Convert the character to lowercase
            lowercase_char = char.lower()
            # Loop through each character in the string starting from index i + 1
            for j in range(i + 1, len(string)):
                # Get the character at index j
                other_char = string[j]
                # If the character is a letter (lowercase or uppercase)
                if other_char.isalpha():
                    # Convert the character to lowercase
                    lowercase_other_char = other_char.lower()
                    # If the two characters are the same (ignoring case)
                    if lowercase_char == lowercase_other_char:
                        # Get the substring of the string starting from index i and ending at index j - 1
                        substr = string[i:j]
                        # If the length of the substring is greater than or equal to n
                        if len(substr) >= n:
                            # Add the substring to the set of palindromes
                            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
