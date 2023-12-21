
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length at least 3 in the given string
    for i in range(2, len(string) - 2):
        # Check if the substring is a palindrome in a case-insensitive manner
        if string[i:i+1].lower() == string[i-1:i+1][::-1].lower():
            # Add the palindrome to the set
            palindromes.add(string[i-1:i+1])
    # Return the set of all palindromes found in the given string
    return palindromes
