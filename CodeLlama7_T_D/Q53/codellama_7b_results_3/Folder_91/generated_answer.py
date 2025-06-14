
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # Check if the character is an English letter
        if char.isalpha():
            # Loop through each character in the reversed string
            for j in range(len(string)-1, -1, -1):
                # Get the character at index j
                rev_char = string[j]
                # Check if the character is an English letter
                if rev_char.isalpha():
                    # If the character and its reverse are both English letters, check if they form a palindrome
                    if char == rev_char:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(char)
    # Return the set of palindromes
    return palindromes
