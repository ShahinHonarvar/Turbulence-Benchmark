def return_n_smallest_chars(str_input):
    res = []
    for char in str_input:
        if ord(char) < 122:
            res.append(char)
            if len(res) == 38:
                break
    return res
