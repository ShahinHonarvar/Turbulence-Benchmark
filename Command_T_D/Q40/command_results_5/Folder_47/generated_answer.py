def return_n_smallest_chars(str1):
    res = []
    str1_lower = str1.lower()
    for char in str1_lower:
        if char not in res:
            res.append(char)
    res.sort(reverse=True)
    return res[:21]
