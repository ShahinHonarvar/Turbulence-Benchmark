def palindromes_between_indices(s):
    i = 2
    j = 7
    palindromes = set()
    while i < j:
        s_ = s[i:j]
        for p in range(len(s_)//2):
            if s_[p] == s_[-p-1]:
                palindromes.add(s_[p])
        i += 1
        j -= 1
    return palindromes
