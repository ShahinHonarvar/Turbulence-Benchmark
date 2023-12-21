
def all_even_ints_inclusive(lst):
    result = []
    for num in lst[:10]:
        if num % 2 == 0:
            result.append(num)
    return result
