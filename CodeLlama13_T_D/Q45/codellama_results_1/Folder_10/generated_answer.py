
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each substring of length 3 to 5 in the given string
    for i in range(len(s) - 2):
        for j in range(i + 3, len(s) + 1):
            # Check if the substring is a palindrome
            if s[i:j] == s[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(s[i:j])

    return palindromes
