
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter (not a space or a digit)
        if char.isalpha():
            # Loop through each character in the reversed substring starting from index i
            for j in range(len(string)-1, i, -1):
                # Get the character at index j
                rev_char = string[j]
                # If the character is a letter (not a space or a digit) and it matches the character at index i
                if rev_char.isalpha() and char == rev_char:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i:j+1])
    return palindromes
