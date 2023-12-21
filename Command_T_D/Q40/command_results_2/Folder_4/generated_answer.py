import string
def return_n_smallest_chars(str1):
    return list(sorted(str1, key = lambda x: ord(x), reverse = True)[:90])
