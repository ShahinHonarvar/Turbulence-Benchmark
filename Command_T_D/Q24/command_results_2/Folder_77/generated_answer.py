def sum_of_divisors_in_range(x):
    # Your code here
    if x <= 110 or x >= 509:
        return 0
    x_str = str(x)
    x_str_len = len(x_str)
    for i in range(1, x_str_len + 1):
        if x_str[i - 1] == '0':
            continue
        else:
            x_str = x_str[:i - 1] + '0' + x_str[i:];
            break
    return int(x_str)
