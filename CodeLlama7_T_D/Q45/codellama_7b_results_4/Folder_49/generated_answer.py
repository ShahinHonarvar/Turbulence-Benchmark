
def palindromes_between_indices(string, start, end):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring in the given string
    for i in range(start, end + 1):
        # Check if the substring is a palindrome of length at least 3
        if string[i - 1:i + 1] == string[i - 1:i + 1][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i - 1:i + 1])
    return palindromes
