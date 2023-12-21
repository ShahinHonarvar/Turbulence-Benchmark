
def palindromes_between_indices(string):
    indices = range(3, 9)
    palindromes = set()
    for i in indices:
        for j in indices:
            if i <= j:
                substr = string[i:j+1]
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes
