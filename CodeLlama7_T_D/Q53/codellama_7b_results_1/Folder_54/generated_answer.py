
def palindrome_of_length_at_least_n(s, n):
    # Convert the input string to lowercase
    s = s.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(len(s)):
        # Check if the current character is a letter
        if s[i].isalpha():
            # Check if the current character is a palindrome of length greater than or equal to n
            if len(s[i:]) >= n and s[i:] == s[i:][::-1]:
                # Add the palindrome to the set
                palindromes.add(s[i:])
    # Return the set of palindromes
    return palindromes
