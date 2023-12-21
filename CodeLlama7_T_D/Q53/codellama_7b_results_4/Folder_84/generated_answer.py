
def palindrome_of_length_at_least_n(s, n):
    # Convert the input string to lowercase
    s = s.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(len(s)):
        # Check if the current character is a letter
        if s[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Loop through each character in the input string, starting from the current index and moving backwards
            for j in range(i, -1, -1):
                # Check if the current character is a letter
                if s[j].isalpha():
                    # Add the current character to the palindrome string
                    palindrome += s[j]
            # Check if the palindrome has a length greater than or equal to the specified minimum length
            if len(palindrome) >= n:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
