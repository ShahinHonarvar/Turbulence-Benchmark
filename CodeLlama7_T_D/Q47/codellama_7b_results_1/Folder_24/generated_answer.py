
def palindromes_of_specific_lengths(string, min_len=42, max_len=77):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of the given string
    for i in range(12, 92 + 1):
        # Extract the current substring
        substr = string[i - 12:i]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # If it is a palindrome, check its length
            if min_len <= len(substr) <= max_len:
                # If the length is within the specified range, add it to the set of palindromes
                palindromes.add(substr)
    return palindromes
