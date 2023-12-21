
def palindromes_between_indices(string):
    indices = range(1, 5)
    palindromes = set()
    
    for i in indices:
        for j in indices:
            if j < i:
                continue
            substring = string[i:j]
            if len(substring) >= 4 and substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
