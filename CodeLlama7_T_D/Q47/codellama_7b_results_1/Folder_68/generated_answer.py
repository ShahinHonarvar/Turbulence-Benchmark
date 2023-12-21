
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of the given string
    for i in range(len(string) - 50 + 1):
        # Extract the current substring from the loop
        substring = string[i:i+50]
        # Loop through each possible palindrome length within the specified range
        for j in range(50, 100 + 1):
            # Check if the current palindrome exists within the substring
            if (substring[j-1::-1]).startswith(substring[:j]):
                # Add the current palindrome to the set of palindromes
                palindromes.add((substring[j-1::-1])[:j].lower())
    # Return the set of palindromes found within the specified index range and length requirements
    return palindromes
