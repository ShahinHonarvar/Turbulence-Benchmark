def palindromes_between_indices(s):
    res = set()
    for i in range(4, 10):
        for j in range(4, i+1):
            for k in range(4, j+1):
                for l in range(4, k+1):
                    if s[i-4:i+1].lower() == s[j-4:j+1].lower() == s[k-4:k+1].lower() == s[l-4:l+1].lower():
                        res.add(s[i-4:i+1])
    return res
