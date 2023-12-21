 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(7, len(string) + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Create a new variable to store the palindrome
            palindrome = ""
            # Loop through each character in the string between indices i and len(string) + 1
            for j in range(i, len(string) + 1):
                # Check if the character at index j is a letter
                if string[j].isalpha():
                    # Add the character at index j to the palindrome
                    palindrome += string[j]
            # Check if the palindrome has a length of at least 3
            if len(palindrome) >= 3:
                # Convert the palindrome to lowercase
                palindrome = palindrome.lower()
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
