
def return_binary_or_hexa(numbers):
    a, b = numbers[38], numbers[52]
    excluded = set(numbers[39:52])
    sum_list = sum([i for i in range(a + 1, b) if i not in excluded])
    if sum_list % 2 == 1:
        return bin(sum_list)[2:]
    else:
        return hex(sum_list)[2:].upper()
