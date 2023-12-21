
def palindromes_of_specific_lengths(string, index_range=(35, 88), palindrome_lengths=(24, 33)):
    # Create a list of all palindromes in the specified index range
    palindromes = []
    for i in range(*index_range):
        substring = string[i:i+1]
        # Check if the current character is a letter
        if substring.isalpha():
            # Create a list of all palindromes with the current character as the center
            palindromes.extend([substring + s + substring for s in substring])
    # Filter out palindromes that are not of the specified lengths
    palindromes = [p for p in palindromes if len(p) in palindrome_lengths]
    return set(palindromes)
