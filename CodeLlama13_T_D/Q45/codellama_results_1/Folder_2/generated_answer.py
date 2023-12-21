
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(1, 6):
        for substring in itertools.combinations(string, i):
            if "".join(substring) == "".join(reversed(substring)):
                palindromes.add("".join(substring))
    return palindromes
