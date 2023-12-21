def palindromes_of_specific_lengths(str):
    res = set()
    for i in range(min(104, len(str)), max(123, len(str))):
        str = str[min(119, i+i):max(i+i, 256)]
        if str == str[::-1]:
            res.add(str)
    return res
