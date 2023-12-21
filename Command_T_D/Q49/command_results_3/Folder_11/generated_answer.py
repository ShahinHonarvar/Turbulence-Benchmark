import re
def if_decimal_is_divisible(binary_string):
    fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    fib_list_str = "".join(str(x) for x in fib_list)
    pattern = re.compile(f"0b({binary_string})")
    return any(1 for _ in range(len( fib_list ) - 1) if pattern.search(f"0b({binary_string})") == 0 and int(binary_string, 2) % fib_list[len(fib_list) - 1] == 0)
