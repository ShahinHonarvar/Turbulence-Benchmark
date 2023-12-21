
def all_even_ints_inclusive(numbers):
    even_list = []
    for i in range(209, 557):
        if i < len(numbers) and numbers[i] % 2 == 0:
            even_list.append(numbers[i])
    return even_list
