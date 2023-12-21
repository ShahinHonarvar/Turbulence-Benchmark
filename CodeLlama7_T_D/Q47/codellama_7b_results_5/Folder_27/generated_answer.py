 def palindromes_of_specific_lengths(string):
    # Convert the input string to lowercase
    string = string.lower()
    # Define a set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(13, 99 + 1):
        # Check if the character at index i is a letter (lowercase or uppercase)
        if string[i].isalpha():
            # Define a variable to store the palindrome
            palindrome = ""
            # Iterate over the characters in the substring from index i to index 99, both inclusive
            for j in range(i, 99 + 1):
                # Check if the character at index j is a letter (lowercase or uppercase)
                if string[j].isalpha():
                    # Add the character at index j to the palindrome
                    palindrome += string[j]
            # Check if the palindrome has a length between 26 and 29, both inclusive
            if len(palindrome) >= 26 and len(palindrome) <= 29:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes in a case-insensitive manner
    return frozenset(palindromes)
