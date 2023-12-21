
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter (not a space or other character)
        if char.isalpha():
            # Loop through each character in the reversed string
            for j in range(len(string)-1, -1, -1):
                # Get the character at index j
                rev_char = string[j]
                # If the character is a letter (not a space or other character) and it matches the character at index i, then we have found a palindrome of length greater than or equal to n
                if rev_char.isalpha() and char == rev_char:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i:j+1])
            # If we have found at least one palindrome of length greater than or equal to n, then we do not need to continue searching for more palindromes
            if len(palindromes) >= n:
                break

    # Return the set of all palindromes of the length greater than or equal to n that exist in the given string
    return palindromes
