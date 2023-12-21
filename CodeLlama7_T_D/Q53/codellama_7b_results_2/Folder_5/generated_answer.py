
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter
        if char.isalpha():
            # Loop through each character in the reversed string
            for j in range(len(string)-1, -1, -1):
                # Get the character at index j
                rev_char = string[j]
                # If the character is a letter and it is not the same as the original character
                if rev_char.isalpha() and rev_char != char:
                    # Check if the palindrome length is greater than or equal to n
                    if len(string[i:j+1]) >= n:
                        # Add the palindrome to the set
                        palindromes.add(string[i:j+1])
    # Return the set of palindromes
    return palindromes
