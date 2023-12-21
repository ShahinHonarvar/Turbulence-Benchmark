
def palindrome_of_length_at_least_n(s, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each word in the string s
    for word in s.split():
        # Check if the word is a palindrome of length greater than or equal to 15
        if len(word) >= n and word == word[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(word)
    # Return the set of palindromes
    return palindromes
