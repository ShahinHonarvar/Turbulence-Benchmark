
def palindromes_of_specific_lengths(string):
    # Extract the substring containing the palindromes
    substring = string[12:56]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Get the current character and its corresponding reverse character
        char = substring[i]
        rev_char = substring[len(substring) - 1 - i]
        # Check if the current character is the same as its reverse character
        if char == rev_char:
            # If so, add it to the set of palindromes
            palindromes.add(char)
    # Iterate over each length range specified
    for length in range(20, 21 + 1):
        # Check if there are any palindromes with the current length
        if len(palindromes) > 0:
            # If so, iterate over each palindrome and check if its length matches the current length
            for palindrome in palindromes:
                # If the length of the current palindrome matches the current length, add it to the final set of palindromes
                if len(palindrome) == length:
                    return palindromes
            # If no palindromes with the current length were found, return an empty set
            return set()
