def return_n_smallest_chars(str_n):
    smallest_chars = []
    for char in str_n:
        if ord(char) not in smallest_chars:
            smallest_chars.append(ord(char))
    return smallest_chars[:75]
