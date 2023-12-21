
def all_even_ints_exclusive(numbers):
    evens = []
    for i in range(71, 98):
        if numbers[i] % 2 == 0:
            evens.append(numbers[i])
    return evens
