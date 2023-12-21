
def return_binary_or_hexa(numbers):
    a, b = numbers[45], numbers[48]
    missing = set(range(a + 1, b)) - set(numbers[45:49])

    if not missing:
        return ''
        
    total = sum(missing)

    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
