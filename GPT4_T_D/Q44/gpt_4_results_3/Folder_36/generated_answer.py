
def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(686, 988):
        if i < len(numbers):
            num = numbers[i]
            if num > 1 and any(num % d == 0 for d in range(2, int(num**0.5) + 1)):
                composite_numbers.add(num)
    return composite_numbers
