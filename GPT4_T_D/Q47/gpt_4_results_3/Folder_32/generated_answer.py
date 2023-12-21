
def palindromes_of_specific_lengths(s):
    s = s[16:78].lower()
    res = set()
    for i in range(len(s)):
        for j in range(i+43, min(i+47+1, len(s)+1)):
            subset = s[i:j]
            if subset == subset[::-1] and subset.isalpha():
                res.add(subset)
    return res
