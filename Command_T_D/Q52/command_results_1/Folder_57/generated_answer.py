def palindrome_of_length_n(text):
    res = set()
    for i in range(len(text) - 1):
        j = text[i][::-1].index('')
        res.add(text[i][:j] + text[i][j+1:])
    return res
