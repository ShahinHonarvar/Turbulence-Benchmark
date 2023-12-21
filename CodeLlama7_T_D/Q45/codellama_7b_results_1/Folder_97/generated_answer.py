
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome
    for i in range(3, len(string) + 1):
        # Loop through each substring of the given string that is of length i and occurs between indices 0 and 4, both inclusive
        for j in range(len(string) - i + 1):
            # Check if the substring is a palindrome
            if string[j:j+i] == string[j:j+i][::-1]:
                # If it is a palindrome, add it to the set of palindromes
                palindromes.add(string[j:j+i])
    return palindromes
