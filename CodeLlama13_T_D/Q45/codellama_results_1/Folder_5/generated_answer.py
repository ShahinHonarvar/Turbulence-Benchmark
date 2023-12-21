
def palindromes_between_indices(s):
    indices = range(4, 9)
    palindromes = set()
    for i in indices:
        for j in indices:
            if j - i + 1 >= 4 and s[i:j+1] == s[i:j+1][::-1]:
                palindromes.add(s[i:j+1])
    return palindromes
