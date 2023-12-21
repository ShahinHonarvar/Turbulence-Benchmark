
def composite_nums_between_indices(numbers):
    composite_numbers = set()

    for i in range(80, 201):
        if i < len(numbers) and is_composite(numbers[i]):
            composite_numbers.add(numbers[i])

    return composite_numbers

def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False
