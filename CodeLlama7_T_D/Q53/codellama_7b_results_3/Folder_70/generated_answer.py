
def palindrome_of_length_at_least_n(string, n):
    # Create a list of all characters in the string
    chars = list(string)
    # Create an empty set to store the palindromes
    palindromes = set()
    # Iterate through each substring of length greater than or equal to n
    for i in range(len(chars) - n + 1):
        # Check if the substring is a palindrome
        if chars[i:i+n] == chars[i:i+n][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(chars[i:i+n])
    # Return the set of palindromes
    return palindromes
