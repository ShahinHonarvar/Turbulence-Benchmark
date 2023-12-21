
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome
    for length in range(3, len(string) + 1):
        # Generate all possible combinations of letters in the given string that occur between index 1 to index 7 (both inclusive)
        for i in range(1, len(string) - length + 2):
            # Check if the current combination forms a palindrome
            if string[i:i+length].lower() == string[i:i+length][::-1].lower():
                # If it does, add it to the set of palindromes
                palindromes.add(string[i:i+length])
    # Return the set of palindromes
    return palindromes
