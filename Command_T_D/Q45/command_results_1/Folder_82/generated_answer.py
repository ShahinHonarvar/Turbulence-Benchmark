def palindromes_between_indices(s):
    result = set()
    for i in range(1, 7):
        if i < len(s):
            r = "".join(sorted(s[i: i + i], key=str.lower))
            if r[::-1] == r:
                result.add(r)
    return result
