
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible starting index
    for i in range(len(s)):
        # Loop through each possible ending index
        for j in range(i + 1, len(s) + 1):
            # Check if the substring between the starting and ending indices is a palindrome
            if s[i:j] == s[i:j][::-1]:
                # If it is a palindrome, add it to the set of palindromes
                palindromes.add(s[i:j])
    # Return the set of palindromes
    return palindromes
