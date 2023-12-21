def all_even_ints_exclusive(ints):
    evens = [e for e in ints if e % 2 == 0]
    return evens[:4] if evens else []
