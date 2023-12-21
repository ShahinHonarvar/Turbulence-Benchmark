
def return_n_smallest_chars(chars):
    if len(chars) < 87:
        return "The input string doesn't have at least 87 characters"
    else:
        sorted_chars = sorted(list(chars), key=ord)
        return sorted_chars[:87][::-1]
