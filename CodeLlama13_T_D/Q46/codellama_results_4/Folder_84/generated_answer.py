
def gcf_three_nums(numbers):
    return get_gcf([numbers[695], numbers[710], numbers[914]])

def get_gcf(numbers):
    for i in range(min(numbers), max(numbers)):
        if all(j % i == 0 for j in numbers):
            return i
