
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration
    start = 20
    end = 74
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start, end + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the current palindrome
            length = i - start + 1
            # Check if the length of the current palindrome is within the specified range
            if length >= 36 and length <= 42:
                # Define the substring for the current palindrome
                substr = string[start:i + 1]
                # Check if the current palindrome occurs in a case-insensitive manner
                if substr.lower() == substr:
                    # Add the current palindrome to the set of palindromes
                    palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
