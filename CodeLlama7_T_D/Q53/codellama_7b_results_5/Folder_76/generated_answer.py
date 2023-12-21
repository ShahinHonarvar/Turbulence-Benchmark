
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Create a substring of the original string starting at the current index and ending at the end of the string
            substr = string[i:]
            # Loop through each character in the substring in reverse order
            for j in range(len(substr)-1, -1, -1):
                # Check if the character is a letter
                if substr[j].isalpha():
                    # Create a substring of the original string starting at the current index and ending at the end of the string
                    palindrome = substr[i:j+1]
                    # Check if the palindrome has a length greater than or equal to n
                    if len(palindrome) >= n:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
