
def all_even_ints_exclusive(numbers):
    even_ints = []
    for i in range(86, 89):
        if numbers[i] % 2 == 0:
            even_ints.append(numbers[i])
    return even_ints
