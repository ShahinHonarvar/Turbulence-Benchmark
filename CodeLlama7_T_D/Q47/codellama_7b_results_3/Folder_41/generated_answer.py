
def palindromes_of_specific_lengths(string):
    # Create a list of all palindromes in the string
    palindromes = []
    for i in range(1, len(string) - 2):
        substring = string[i:i+4]
        if substring == substring[::-1]:
            palindromes.append(substring)
    # Return the set of all palindromes with lengths between 3 and 4
    return set(palindromes)
