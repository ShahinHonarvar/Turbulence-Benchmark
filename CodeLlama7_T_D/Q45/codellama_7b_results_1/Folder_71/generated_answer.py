
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # Check if the character is a letter (not whitespace or punctuation)
        if char.isalpha():
            # Get the lowercase version of the character
            lowercase_char = char.lower()
            # Loop through each character in the string starting from index i + 1
            for j in range(i + 1, len(string)):
                # Get the character at index j
                other_char = string[j]
                # Check if the other character is a letter (not whitespace or punctuation)
                if other_char.isalpha():
                    # Get the lowercase version of the other character
                    lowercase_other_char = other_char.lower()
                    # Check if the lowercase version of the character is the same as the lowercase version of the other character
                    if lowercase_char == lowercase_other_char:
                        # If the length of the substring starting at index i and ending at index j is at least 4, add it to the set of palindromes
                        if j - i + 1 >= 4:
                            # Add the substring starting at index i and ending at index j to the set of palindromes
                            palindromes.add(string[i:j+1])
    # Return the set of palindromes
    return palindromes
