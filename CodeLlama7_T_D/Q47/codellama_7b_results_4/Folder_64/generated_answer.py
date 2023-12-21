 def palindromes_of_specific_lengths(string, index_range, lengths):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string within the specified index range
    for i in range(*index_range):
        # Check if the current character is a palindrome with one of the specified lengths
        if len(string[i:]) >= 4 and all(len(string[i:].lower()) == length for length in lengths)):
            # Add the palindrome to the set
            palindromes.add(string[i:].lower())
    return palindromes
