def palindromes_between_indices(s):
    result = set()
    for i in range(0, len(s) + 1):
        for j in range(i, len(s) + 1):
            if i == j:
                continue
            for k in range(j, len(s) + 1):
                for l in range(k, len(s) + 1):
                    if i == l:
                        continue
                    if j == k:
                        continue
                    if j == l:
                        continue
                    if k == l:
                        continue
                    if s[i:j] == s[k:l] == s[i:l] == s[k:j]:
                        result.add(s[i:j])
    return result
