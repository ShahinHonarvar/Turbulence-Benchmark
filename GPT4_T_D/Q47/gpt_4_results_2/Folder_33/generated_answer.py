
def palindromes_of_specific_lengths(s):
    import string
    s = s[130:296].lower()
    letters = set(string.ascii_lowercase)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+103, min(i+159, len(s) + 1)):
            subset = s[i:j]
            if set(subset).issubset(letters) and subset == subset[::-1]:
                palindromes.add(subset)
    return palindromes
