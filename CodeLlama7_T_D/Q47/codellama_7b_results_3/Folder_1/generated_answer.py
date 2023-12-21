
def palindromes_of_specific_lengths(string):
    # Split the string into a list of substrings
    substrings = string.split()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each substring in the list
    for substring in substrings:

        # Check if the substring is a palindrome
        if substring == substring[::-1]:

            # If it is, add it to the set of palindromes
            palindromes.add(substring)

    # Return the set of palindromes that meet the specified criteria
    return palindromes
