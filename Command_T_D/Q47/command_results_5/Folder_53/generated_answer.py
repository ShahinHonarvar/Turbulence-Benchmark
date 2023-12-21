def palindromes_of_specific_lengths(str):
    res = set()
    for i in range(1, 300):
        for j in range(i + 1, 300):
            for k in range(j + 1, 300):
                for l in range(k + 1, 300):
                    if str[i:j] == str[j:k] == str[k:l] == str[l:]:
                        res.add(str[i:j])
    return res
