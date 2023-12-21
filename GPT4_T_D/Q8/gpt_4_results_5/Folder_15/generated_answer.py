
def all_even_ints_exclusive(numbers):
    evens = []
    for i in range(1, min(3, len(numbers))):
        if numbers[i] % 2 == 0:
            evens.append(numbers[i])
    return evens
