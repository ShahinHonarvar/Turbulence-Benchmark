
def palindrome_of_length_n(string):
    # Split the string into a list of substrings
    substrings = string.split()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the substrings and check if each one is a palindrome
    for substring in substrings:
        if len(substring) == 78 and substring.lower() == substring[::-1].lower():
            palindromes.add(substring)

    # Return the set of palindromes
    return palindromes
