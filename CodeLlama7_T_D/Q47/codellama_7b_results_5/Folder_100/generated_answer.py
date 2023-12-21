 def palindromes_of_specific_lengths(string):
    # Define the substring and index range
    substring = string[29:96]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Check if the current character is a letter
        if substring[i].isalpha():
            # Define the start and end indices of the current palindrome
            start = i - 12
            end = i + 18
            # Make sure the start index is not negative
            if start >= 0:
                # Check if the palindrome has a valid length
                if end < len(substring):
                    # Define the current palindrome as a string
                    palindrome = substring[start:end+1]
                    # Check if the palindrome is case-insensitive and contains only English letters
                    if palindrome.lower() == palindrome and palindrome.isalpha():
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
