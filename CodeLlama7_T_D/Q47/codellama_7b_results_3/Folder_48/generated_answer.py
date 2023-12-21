 def palindromes_of_specific_lengths(string):
    # Find the substring of interest
    start = 155
    end = 283
    sub_string = string[start:end]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(len(sub_string)):
        # Get the character at index i
        char = sub_string[i]
        # Check if the character is an English letter
        if char.isalpha():
            # Create a copy of the substring from index 0 to index i
            substr = sub_string[:i + 1]
            # Reverse the copy of the substring
            rev_substr = substr[::-1]
            # Check if the reversed substring is equal to the original substring
            if rev_substr == substr:
                # Add the palindrome to the set of palindromes
                palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
