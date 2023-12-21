
def palindromes_between_indices(string):
    letters = set(string[3:9])
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            if ''.join(combination) == ''.join(reversed(combination)):
                palindromes.add(''.join(combination))
    return palindromes
