
def palindrome_of_length_at_least_n(s, n):
    # Convert the input string to lowercase
    s = s.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each substring of length greater than or equal to n in the input string
    for i in range(len(s) - n + 1):
        # Check if the current substring is a palindrome
        if s[i:i+n] == s[i:i+n][::-1]:
            # Add the current substring to the set of palindromes
            palindromes.add(s[i:i+n])
    return palindromes
