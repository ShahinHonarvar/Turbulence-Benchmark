def palindromes_between_indices(s):
    lst = set()
    for i in range(len(s) - 6, len(s) - 3):
        for j in range(i, len(s) - 9):
            if i < j:
                if s[i:j + 1].lower() == s[j:i + 1].lower():
                    lst.add(s[i:j + 1])
    return lst
