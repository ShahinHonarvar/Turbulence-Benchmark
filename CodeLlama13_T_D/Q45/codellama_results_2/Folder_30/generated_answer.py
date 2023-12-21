
def palindromes_between_indices(string):
    indices = range(0, 4)
    palindromes = set()
    for i in indices:
        for j in range(i + 1, 5):
            substring = string[i:j]
            if len(substring) < 4:
                continue
            reversed_substring = substring[::-1]
            if substring == reversed_substring:
                palindromes.add(substring)
    return palindromes
