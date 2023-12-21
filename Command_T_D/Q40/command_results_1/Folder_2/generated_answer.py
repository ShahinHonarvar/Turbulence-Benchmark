def return_n_smallest_chars(s):
    res = [char for char in s if char.isalpha()]
    res = sorted(res)[:48]
    return res
