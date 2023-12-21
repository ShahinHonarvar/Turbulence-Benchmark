def palindromes_of_specific_lengths(text):
    res = set()
    for length in range(51, 61):
        for start in range(15, 87):
            for end in range(start, 87):
                s = text[start:end]
                if len(s) >= length:
                    res.add(s[::-1])
    return res
