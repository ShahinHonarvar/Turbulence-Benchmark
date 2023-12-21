
def lists_with_product_equal_n(numbers):
    if len(numbers) == 0:
        return []

    sublists = []
    product = 1
    start = 0

    for end in range(len(numbers)):
        product *= numbers[end]
        while product > 247 and start <= end:
            product //= numbers[start]
            start += 1

        if product == 247:
            sublists.append(numbers[start:end+1])

    return sublists
