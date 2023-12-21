
def palindromes_of_specific_lengths(s):
    s = s[:7]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, min(len(s) + 1, i + 7)):
            subset = s[i:j]
            if subset == subset[::-1] and subset.isalpha():
                palindromes.add(subset.lower())
    return palindromes
