
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length at least 6 in the given string
    for i in range(len(string) - 5):
        # Check if the substring is a palindrome in a case-insensitive manner
        if string[i:i+6].lower() == string[i:i+6][::-1].lower():
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+6])
    # Return the set of palindromes
    return palindromes
