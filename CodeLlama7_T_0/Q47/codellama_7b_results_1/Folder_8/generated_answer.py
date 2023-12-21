
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration
    start = 17
    end = 72
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start, end + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the current palindrome
            length = i - start + 1
            # Check if the length is within the specified range
            if length >= 50 and length <= 51:
                # Define the substring for the current palindrome
                substr = string[start:i + 1]
                # Check if the substring is a palindrome in a case-insensitive manner
                if substr == substr[::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
