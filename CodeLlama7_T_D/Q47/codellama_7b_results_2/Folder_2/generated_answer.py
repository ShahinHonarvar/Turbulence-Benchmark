 def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each character in the string
    for i in range(10, 59 + 1):
        # Check if the substring starting at index i and ending at index 59 is a palindrome
        substr = string[i:59]
        if substr == substr[::-1]:
            # If it is a palindrome, check its length
            if len(substr) in range(18, 36 + 1):
                # If the length is within the specified range, add it to the set of palindromes
                palindromes.add(substr)
    return palindromes
