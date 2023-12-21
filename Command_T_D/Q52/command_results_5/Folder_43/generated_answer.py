def palindrome_of_length_n(str):
    res = set()
    for i in range(len(str)):
        for j in range(i, len(str)):
            res.add(str[i:j])
    return res
