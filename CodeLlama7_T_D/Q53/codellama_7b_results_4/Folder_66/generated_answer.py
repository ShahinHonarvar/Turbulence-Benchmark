
def palindrome_of_length_at_least_n(s, n):
    # Convert the input string to lowercase
    s = s.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the input string
    for i in range(len(s)):
        # Check if the character at position i is a letter
        if s[i].isalpha():
            # Iterate over the remaining characters in the input string
            for j in range(i + 1, len(s) + 1):
                # Check if the substring starting at position i and ending at position j is a palindrome
                if s[i:j] == s[i:j][::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(s[i:j])
    # Return the set of palindromes that have a length greater than or equal to n
    return palindromes
