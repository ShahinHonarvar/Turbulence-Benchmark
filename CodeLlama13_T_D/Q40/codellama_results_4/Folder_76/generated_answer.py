
def return_n_smallest_chars(string):
    lst = []
    for char in string:
        if char not in lst:
            lst.append(char)
    lst.sort()
    return lst[:3]
