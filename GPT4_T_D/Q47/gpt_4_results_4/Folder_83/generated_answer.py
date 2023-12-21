
def palindromes_of_specific_lengths(s):
    from re import sub
    s = s[75:96].lower()
    s = sub(r'[^a-z]', '', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+7, min(i+10, len(s)+1)):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
