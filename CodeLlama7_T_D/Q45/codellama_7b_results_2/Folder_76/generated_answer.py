
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length at least 4 in the given string
    for i in range(len(string) - 3):
        # Extract the substring from the current index to the end of the string
        substring = string[i:len(string)]
        # Check if the substring is a palindrome by comparing it with its reverse
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
