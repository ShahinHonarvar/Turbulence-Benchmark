def palindromes_between_indices(s):
    return set(
        p for i in range(2, len(s)-5) for j in range(i+1, len(s)-4)
        for p in (''.join(sorted(set(s[i:j+1:2]))),
                  ''.join(sorted(set(s[i:j+2:2]))),
                  ''.join(sorted(set(s[i:j+3:2]))))
