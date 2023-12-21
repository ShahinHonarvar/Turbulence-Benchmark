def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(15, 89):
        if i >= 40 and i <= 72:
            for j in range(i, i + i // 2):
                if s[j].lower() == s[j][::-1].lower():
                    res.add(s[j])
    return res
