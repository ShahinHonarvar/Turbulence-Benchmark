
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Loop through each character in the reversed substring starting from the current character
            for j in range(i, len(string) - 1, -1):
                # Check if the current character and the next character form a palindrome of length greater than or equal to n
                if string[i].lower() == string[j].lower() and (j - i + 1) >= n:
                    # Add the palindrome to the set
                    palindromes.add(string[i:j+1])
    # Return the set of all palindromes of length greater than or equal to n that exist in the given string
    return palindromes
