
def all_even_ints_inclusive(numbers):
    even_numbers = []
    for i in range(10, min(len(numbers), 67)):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
    return even_numbers
