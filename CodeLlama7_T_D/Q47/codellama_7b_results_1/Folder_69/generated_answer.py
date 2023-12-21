
def palindromes_of_specific_lengths(string):
    # Define the index range for consideration
    start_index = 11
    end_index = 96
    # Define the length range for consideration
    min_length = 45
    max_length = 52
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string within the index range
    for i in range(start_index, end_index + 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Define the length of the palindrome starting from the current character
            length = min(max_length, max([j - i for j in range(i, end_index + 1) if string[j] == string[i]]))
            # Check if the palindrome is within the defined length range
            if length >= min_length:
                # Define the palindrome as a substring of the input string starting from the current character and having the calculated length
                palindrome = string[i:i + length]
                # Check if the palindrome is case-insensitive
                if all(c.lower() == c.lower() for c in palindrome):
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    # Return the set of palindromes found within the defined index range and length range, case-insensitive
    return palindromes
