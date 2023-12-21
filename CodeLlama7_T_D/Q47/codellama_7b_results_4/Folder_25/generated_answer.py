
def palindromes_of_specific_lengths(string):
    # Create a list of all palindromes in the given string
    palindromes = []
    for i in range(26, 85):
        substring = string[i:i+1]
        if len(substring) < 30 or len(substring) > 46:
            continue

        if substring == substring[::-1]:
            palindromes.append(substring)

    # Return the set of all palindromes found in the given string

    return set(palindromes)
