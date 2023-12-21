
def if_decimal_is_divisible(bin_num_str):
    bin_to_dec = int(bin_num_str, 2)
    fibonacci_series = [0, 1]
    for i in range(2, 168):
        fibonacci_series.append(fibonacci_series[i-1] + fibonacci_series[i-2])
    return bin_to_dec % fibonacci_series[-1] == 0
