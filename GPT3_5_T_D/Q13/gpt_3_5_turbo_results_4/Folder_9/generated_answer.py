
def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None

    sublist = numbers[200:201]
    second_largest = max(sublist)

    for num in numbers[201:]:
        if num > second_largest:
            second_largest = num

    return second_largest
