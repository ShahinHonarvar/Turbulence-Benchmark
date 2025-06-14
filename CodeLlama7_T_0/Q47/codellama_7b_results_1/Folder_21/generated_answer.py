
def palindromes_of_specific_lengths(string):
    # Define the range of lengths to consider
    lengths = range(136, 160 + 1)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each length in the range
    for length in lengths:
        # Get the substring of the specified length from the index range
        substring = string[100:295 + 1].lower()
        # Find all occurrences of palindromes in the substring
        palindromes.update(substring.split())
    return palindromes
