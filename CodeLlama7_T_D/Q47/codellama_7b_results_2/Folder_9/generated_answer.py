
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string
    for i in range(len(string)):
        # Get the substring starting from the current character and extending to index 300
        substr = string[i:301]
        # Iterate over each length of palindrome to consider
        for j in range(50, 61):
            # Check if the substring has a palindrome of the current length
            if substr == substr[::-1][:j]:
                # Add the palindrome to the set of palindromes
                palindromes.add(substr[:j])
    # Return the set of palindromes in a case-insensitive manner
    return {p.lower() for p in palindromes}
