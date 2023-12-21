def return_n_smallest_chars(str):
    return list(sorted(str, key=lambda x: ord(x), reverse=True)[:24])
