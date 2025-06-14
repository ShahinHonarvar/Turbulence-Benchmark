
def palindromes_between_indices(s):
    palindromes = set()
    for i in range(5, 9):
        for j in range(i+1, len(s)):
            if s[i:j].lower() == s[i:j][::-1].lower():
                palindromes.add(s[i:j])
    return palindromes
