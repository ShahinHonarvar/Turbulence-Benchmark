
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at position i
        char = string[i]
        # Check if the character is a letter (not a space or punctuation)
        if char.isalpha():
            # Get the reverse of the character
            rev_char = char[::-1]
            # Loop through each character in the reverse of the character
            for j in range(len(rev_char)):
                # Get the character at position j in the reverse of the character
                char2 = rev_char[j]
                # Check if the character is a letter (not a space or punctuation)
                if char2.isalpha():
                    # Concatenate the character and its reverse to form a palindrome
                    palindrome = char + char2
                    # Check if the palindrome has a length greater than or equal to n
                    if len(palindrome) >= n:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
