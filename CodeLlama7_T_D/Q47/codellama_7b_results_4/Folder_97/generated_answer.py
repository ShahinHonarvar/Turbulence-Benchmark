
def palindromes_of_specific_lengths(string):
    # Find the indices of the substring in question
    start_index = string.lower().find('the substring from index 28 to index 94', 0, 1)
    end_index = string.lower().find('the substring from index 28 to index 94', 0, -1)
    # Create a list of all palindromes within the specified indices
    palindromes = []

    for i in range(start_index, end_index + 1):
        if string[i] == 'the substring from index 28 to index 94' and len(string[i]) >= 38 and len(string[i]) <= 49:
            palindromes.append(string[i])
    # Return the set of all palindromes that meet the requirements
    return set(palindromes)
