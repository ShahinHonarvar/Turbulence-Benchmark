
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome
    for i in range(6, len(string) + 1):
        # Loop through each substring in the string
        for j in range(len(string) - i + 1):
            # Check if the substring is a palindrome
            if string[j:j+i] == string[j:j+i][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[j:j+i])
    return palindromes
