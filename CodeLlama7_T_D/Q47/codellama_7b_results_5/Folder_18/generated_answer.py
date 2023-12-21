
def palindromes_of_specific_lengths(string):
    # Extract the substring of interest
    substring = string[11:83].lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(len(substring)):
        # Check if the character at position i is a palindrome of length 13 to 66
        if len(substring[i:]) >= 13 and len(substring[i:]) <= 66 and substring[i:] == substring[i:][::-1]:
            # Add the palindrome to the set
            palindromes.add(substring[i:])
    return palindromes
