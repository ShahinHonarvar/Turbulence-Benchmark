
def palindromes_of_specific_lengths(string):
    # Define the range of lengths to consider
    lengths = range(104, 121)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each length in the range
    for length in lengths:
        # Get the substring of the specified length from the index range
        substring = string[155:283]
        # Find all palindromes in the substring using a case-insensitive regular expression
        palindromes.update(re.findall(r"(\w{" + str(length) + r"})\w*\1", substring, re.IGNORECASE)))
    return palindromes
