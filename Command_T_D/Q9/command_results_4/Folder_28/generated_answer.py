def all_odd_ints_inclusive(ints):
    try:
        return [x for x in range(63, -1, 2) if x in ints]
    except:
        pass
