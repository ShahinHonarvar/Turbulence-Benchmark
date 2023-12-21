
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their greatest common divisor

    num1 = my_list[69]
    num2 = my_list[40]
    min_val = min(num1, num2)
    max_val = max(num1, num2)
    for i in range(2, min_val + 1):
        if min_val % i == 0 and max_val % i == 0:
            gcf = i

    return gcf
