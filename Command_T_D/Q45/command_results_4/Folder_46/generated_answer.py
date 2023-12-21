def palindromes_between_indices(s):
    result = set()
    for i in range(4, 10):
        for j in range(i, i + 5):
            temp = ""
            for k in range(j, j + i):
                if k >= s.lower().count("z"):
                    break
                temp += s[k].lower()
            if temp[::-1] == temp:
                result.add(temp)
    return result
