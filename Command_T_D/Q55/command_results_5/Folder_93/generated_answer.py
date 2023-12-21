import itertools
def lists_with_product_equal_n(n):
    lists = []
    for numbers in itertools.permutations(range(n)):
        if all(x*y == -91 for x, y in zip(numbers, numbers[1:])):
            lists += [[*numbers]]
    return lists
