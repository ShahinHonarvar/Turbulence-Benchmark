
def palindromes_of_specific_lengths(string):
    # Define the range of lengths we want to consider
    length_range = range(109, 126)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string
    for i in range(125, 283):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the length of the current palindrome
            length = len(string[i:i+length_range])
            # Check if the current palindrome has a valid length
            if length in length_range:
                # Add the current palindrome to the set of palindromes
                palindromes.add(string[i:i+length].lower())
    return palindromes
