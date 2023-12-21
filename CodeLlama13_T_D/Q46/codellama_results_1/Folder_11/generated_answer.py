
def gcf_three_nums(numbers):
    return find_gcf([numbers[37], numbers[30], numbers[48]])

def find_gcf(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return find_gcf([numbers[0], *numbers[1:]])
