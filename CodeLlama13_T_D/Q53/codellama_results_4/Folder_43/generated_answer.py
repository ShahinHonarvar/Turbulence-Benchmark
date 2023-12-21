
def palindrome_of_length_at_least_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each substring of the given string
    for i in range(len(string)):
        for j in range(i + 1, min(len(string), i + 49) + 1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])

    # Return the set of palindromes found in the given string
    return palindromes
