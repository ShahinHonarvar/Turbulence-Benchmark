
def palindromes_of_specific_lengths(string):
    # Create a substring of the input string that contains the desired index range
    substring = string[26:90]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Check if the current character is a letter (i.e., not a space or punctuation mark)
        if substring[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Iterate over each character in the substring, starting from the current index and moving backwards until reaching the beginning of the substring
            for j in range(i, -1, -1):
                # Check if the current character is a letter (i.e., not a space or punctuation mark)
                if substring[j].isalpha():
                    # Add the current character to the palindrome string
                    palindrome += substring[j]
            # Check if the palindrome has the desired length
            if len(palindrome) >= 27 and len(palindrome) <= 58:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes in a case-insensitive manner
    return frozenset([x.lower() for x in palindromes])
