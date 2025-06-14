 def palindromes_of_specific_lengths(string):
    # Define the range of lengths for palindromes
    lengths = range(24, 33 + 1)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(35, 89 + 1):
        # Check if the character at index `i` is a letter
        if string[i].isalpha():
            # Define a variable to store the palindrome
            palindrome = ""
            # Iterate over the characters in the substring
            for j in range(i, i + 10):
                # Check if the character at index `j` is a letter
                if string[j].isalpha():
                    # Add the character to the palindrome
                    palindrome += string[j]
            # Check if the palindrome has a length in the specified range
            if len(palindrome) in lengths:
                # Convert the palindrome to lowercase
                palindrome = palindrome.lower()
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    return palindromes
