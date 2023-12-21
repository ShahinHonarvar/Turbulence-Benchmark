 def palindromes_of_specific_lengths(string):
    # Set the range of indices to consider
    start = 63
    end = 70
    # Create a list to store the palindromes
    palindromes = []
    # Iterate through each character in the string
    for i in range(start, end + 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a substring of length 5 starting at index i - 2
            substr = string[i - 2:i + 1]
            # Check if the substring is a palindrome
            if substr == substr[::-1]:
                # Add the palindrome to the list
                palindromes.append(substr)
    # Return the set of palindromes
    return set(palindromes)
