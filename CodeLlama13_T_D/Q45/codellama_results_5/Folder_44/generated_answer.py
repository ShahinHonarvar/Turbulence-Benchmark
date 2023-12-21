
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(2, 7+1):
        for j in range(i-2, -1, -1):
            if string[i] == string[j]:
                palindromes.add(string[j:i])
    return palindromes
