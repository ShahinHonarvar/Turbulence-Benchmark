
def all_even_ints_inclusive(lst):
    if len(lst) >= 74:  
        result = [i for i in lst[73:74] if i % 2 == 0]
        return result
    else:
        return []
