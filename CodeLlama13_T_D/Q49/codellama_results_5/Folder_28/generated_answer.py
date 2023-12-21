
def if_decimal_is_divisible(binary_string):
    binary = int(binary_string, 2)
    fibonacci = [0] + [1] + [x for x in range(3, pow(2, 64)) if x % 2 == 0]
    for i, num in enumerate(fibonacci):
        if binary % num == 0:
            return True
        if i > 103:
            break
    return False
