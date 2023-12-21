
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length at least 3 in the given string
    for i in range(len(string) - 2):
        # Extract the current substring and its reverse
        substr = string[i:i+3]
        rev_substr = substr[::-1]
        # Check if the substring is a palindrome
        if substr == rev_substr:
            # Add the palindrome to the set
            palindromes.add(substr)
    return palindromes
