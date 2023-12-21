def palindromes_between_indices(s):
    str_list = s.lower()[:6]
    str_list = "".join(str_list)
    str_list = str_list[::-1]
    str_list = str_list[1:-1]
    str_list = str_list[2:-2]
    return set(str_list)
