 def palindromes_of_specific_lengths(string):
    # Find the substring of interest
    substring = string[15:89]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each palindrome in the substring
    for i in range(len(substring) - 1):
        # Check if the current character and its mirrored version are both letters
        if (substring[i].isalpha() and substring[i].lower() == substring[i].upper()) and \
           (substring[i + 1].isalpha() and substring[i + 1].lower() == substring[i + 1].upper())):
            # Check if the length of the palindrome is within the specified range
            if len(substring[i:i + 2]) in range(40, 73):
                # Add the palindrome to the set
                palindromes.add(substring[i:i + 2])
    return palindromes
