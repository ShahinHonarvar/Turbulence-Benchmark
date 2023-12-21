
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration
    start = 23
    end = 77
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start, end + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the palindrome
            length = min(end - start + 1, 40)
            # Iterate over the possible lengths of the palindrome
            for j in range(length):
                # Check if the character at index i + j is a letter
                if string[i + j].isalpha():
                    # Define the palindrome as the substring from index i to index i + j, inclusive
                    palindrome = string[i:i + j + 1]
                    # Check if the palindrome is of the specified length and consists only of English letters
                    if len(palindrome) == length and all(c.isalpha() for c in palindrome):
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)
    # Return the set of palindromes found in the specified index range
    return palindromes
