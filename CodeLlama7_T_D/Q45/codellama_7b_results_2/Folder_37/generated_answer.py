
def palindromes_between_indices(s):
    # Define a set to store all palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(s)):
        # Get the substring that starts at index i and ends at index len(s) - 1
        substr = s[i:len(s)]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)
    return palindromes
