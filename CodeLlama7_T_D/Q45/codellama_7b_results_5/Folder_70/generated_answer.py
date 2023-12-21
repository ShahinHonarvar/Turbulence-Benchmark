
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string
    for i in range(len(s)):
        # Get the character at index i
        c = s[i]
        # Check if the character is a letter
        if c.isalpha():
            # Get the lowercase version of the character
            lc = c.lower()
            # Iterate over each character in the string starting from index i + 1
            for j in range(i + 1, len(s)):
                # Get the character at index j
                d = s[j]
                # Check if the character is a letter
                if d.isalpha():
                    # Get the lowercase version of the character
                    ld = d.lower()
                    # Check if the lowercase version of the characters are equal
                    if lc == ld:
                        # Form a palindrome by concatenating the characters at indices i and j
                        palindrome = s[i:j+1]
                        # Add the formed palindrome to the set of palindromes
                        palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
