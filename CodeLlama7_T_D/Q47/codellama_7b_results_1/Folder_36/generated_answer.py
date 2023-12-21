 def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the specified index range
    for i in range(124, 283 + 1):
        # Check if the character at position i is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Check if the character at position i is the same as the character at position i - 1 (accounting for wrap-around)
            if string[i] == string[(i - 1) % len(string)]:
                # Check if the character at position i + 1 is a letter (uppercase or lowercase)
                if string[i + 1].isalpha():
                    # Check if the character at position i + 1 is the same as the character at position i - 1 (accounting for wrap-around)
                    if string[i + 1] == string[(i - 1) % len(string)]:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(string[i:i + 2])
    return palindromes
