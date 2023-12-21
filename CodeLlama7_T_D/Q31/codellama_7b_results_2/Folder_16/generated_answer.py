
def if_perfect_num(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Check if the element at index 162 is a perfect number
    try:
        num = my_list[162]
        # Check if the number is divisible by all numbers up to its square root
        for i in range(1, int(num ** 0.5) + 1):
            if num % i != 0:
                raise ValueError("Number at index 162 is not a perfect number")
    except IndexError:
        return False
