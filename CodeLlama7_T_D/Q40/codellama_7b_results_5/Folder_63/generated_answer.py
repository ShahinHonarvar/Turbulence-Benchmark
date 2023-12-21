
def return_n_smallest_chars(s, n):
    # sort the string in ascending order based on ASCII values
    s = sorted(s)
    # create a list of exactly 44 characters of the given string
    return_list = []
    for i in range(n):
        return_list.append(s[i])
    return return_list
