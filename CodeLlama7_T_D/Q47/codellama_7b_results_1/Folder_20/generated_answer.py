
def palindromes_of_specific_lengths(string):
    # Find the substring of interest
    substring = string[20:74]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Get the current character and its reverse
        char = substring[i]
        rev_char = substring[len(substring) - 1 - i]
        # If the character and its reverse are the same, add it to the set of palindromes
        if char == rev_char:
            palindromes.add(char)
    # Filter the palindromes based on their length
    filtered_palindromes = {x for x in palindromes if len(x) >= 36 and len(x) <= 42}
    return filtered_palindromes
