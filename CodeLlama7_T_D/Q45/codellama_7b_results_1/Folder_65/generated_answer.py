
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring that starts at index i and ends at index len(string) - 1
        substring = string[i:len(string)]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    return palindromes
