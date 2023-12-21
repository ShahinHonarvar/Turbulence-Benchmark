
def all_odd_ints_exclusive(numbers):
    odd_ints = []
    for num in numbers[1:3]:
        if num % 2 != 0:
            odd_ints.append(num)
    return odd_ints
