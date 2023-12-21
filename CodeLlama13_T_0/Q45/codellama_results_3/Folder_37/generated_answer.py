
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(1, 4):
        for j in range(i+5, len(string)+1):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
