
def palindromes_of_specific_lengths(string):
    # Create a substring of the specified index range
    substring = string[125:283]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Get the current character and its reverse
        char = substring[i]
        rev_char = substring[i:][::-1]
        # If the current character is the same as its reverse, add it to the set of palindromes
        if char == rev_char:
            palindromes.add(char)
    return palindromes
