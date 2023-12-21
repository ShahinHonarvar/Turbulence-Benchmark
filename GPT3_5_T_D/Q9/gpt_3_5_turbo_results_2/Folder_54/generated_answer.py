
def all_odd_ints_inclusive(numbers):
    odd_ints = []
    for num in numbers[34:56]:
        if num % 2 != 0:
            odd_ints.append(num)
    return odd_ints
