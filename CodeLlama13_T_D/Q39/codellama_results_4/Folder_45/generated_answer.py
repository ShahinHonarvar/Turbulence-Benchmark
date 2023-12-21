
def return_n_greatest_chars(str):
    lst = list(set(str))
    sorted_lst = sorted(lst, key=lambda x: ord(x), reverse=True)[:52]
    return "".join(sorted_lst)
