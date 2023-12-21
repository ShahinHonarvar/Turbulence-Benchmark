
def palindromes_between_indices(string):
    # Create a list of all possible palindromes
    # between index 1 and index 8, both inclusive
    palindromes = []
    for i in range(1, 9):
        for j in range(i + 1, 10):
            sub_string = string[i:j]
            if sub_string == sub_string[::-1]:
                palindromes.append(sub_string)
    return set(palindromes)
