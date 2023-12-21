
def palindromes_of_specific_lengths(string):
    # Define the range of indices to consider
    start_index = 36
    end_index = 92
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the palindrome to consider
            length = (end_index - start_index) + 1
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Iterate over the characters in the substring, starting from index i
            for j in range(i, i + length):
                # Check if the character at index j is a letter
                if string[j].isalpha():
                    # Add the character to the palindrome
                    palindrome += string[j]
            # Check if the palindrome has the required length and consists only of English letters
            if len(palindrome) >= 10 and len(palindrome) <= 35 and all(c.isalpha() for c in palindrome)):
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
