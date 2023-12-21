
def return_n_greatest_chars(s):
    if (len(set(s)) >= 68):
        sorted_list = sorted(s, key = lambda x: ord(x))
        return sorted_list[-68:]
    else:
        return "The input should contain at least 68 distinct characters."
