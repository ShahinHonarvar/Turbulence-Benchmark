
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible starting index in the string
    for i in range(len(string) - 5 + 1):
        # Loop through each possible ending index in the string
        for j in range(i + 6, len(string) + 1):
            # Check if the substring between indices i and j is a palindrome
            substring = string[i:j]
            if substring == substring[::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(substring)
    return palindromes
