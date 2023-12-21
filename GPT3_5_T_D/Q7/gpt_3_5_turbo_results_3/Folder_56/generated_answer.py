
def all_even_ints_inclusive(lst):
    evens = [num for num in lst if num % 2 == 0]
    return evens[:1] if len(evens) > 0 else []
