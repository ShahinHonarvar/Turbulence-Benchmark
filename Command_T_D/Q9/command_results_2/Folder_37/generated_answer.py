def all_odd_ints_inclusive(ints):
    return [x for x in range(1, len(ints)+1) if int(x)%2!=0 and x in ints]
