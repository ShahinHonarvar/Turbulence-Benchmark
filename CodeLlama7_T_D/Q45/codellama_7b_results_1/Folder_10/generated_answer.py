
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each letter in the string
    for i in range(len(s)):
        # Get the current letter
        c = s[i]
        # If the current letter is not a letter, skip it
        if not c.isalpha():
            continue

        # Loop through each letter in the reverse of the string
        for j in range(len(s)-1, -1, -1):
            # Get the current letter in the reverse string
            d = s[j]
            # If the current letter is not a letter, skip it
            if not d.isalpha():
                continue

            # Check if the current letters are the same and the next letter is not a letter
            if c == d and not s[i+1].isalpha():
                # Add the palindrome to the set of palindromes
                palindromes.add(s[i:j+1])
    # Return the set of palindromes
    return palindromes
