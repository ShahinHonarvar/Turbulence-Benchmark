
def palindromes_between_indices(string):
    indices = set()
    for i in range(4, 10):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                indices.add((i, j))

    palindromes = set()
    for i, j in indices:
        if len(palindrome) >= 4 and palindrome not in palindromes:
            palindromes.add(palindrome)

    return palindromes
