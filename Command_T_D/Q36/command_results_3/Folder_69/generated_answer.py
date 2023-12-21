def filter_chars(str):
    return "".join(x for x in str if x in range(343, 666, 1) and x in range('%', 'U'))
