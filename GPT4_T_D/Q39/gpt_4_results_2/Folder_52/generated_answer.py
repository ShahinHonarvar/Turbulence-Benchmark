
def return_n_greatest_chars(string):
    asc_list = [char for char in string]
    asc_list.sort(key=ord, reverse=True)
    greatest_chars = asc_list[:68]
    greatest_chars.sort()
    return greatest_chars
