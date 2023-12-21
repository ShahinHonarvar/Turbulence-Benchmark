
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at position i
        char = string[i]
        # If the character is a letter, add it to the set of characters to check for palindromes
        if char.isalpha():
            palindrome_chars.add(char)
    # Loop through each pair of characters in the set of palindrome characters
    for i in range(len(palindrome_chars)):
        for j in range(i + 1, len(palindrome_chars)):
            # If the two characters are the same and have a length greater than or equal to n, add them to the set of palindromes
            if palindrome_chars[i] == palindrome_chars[j] and len(palindrome_chars[i]) >= n:
                palindromes.add((palindrome_chars[i], palindrome_chars[j]))
    # Return the set of palindromes
    return palindromes
