
def if_perfect_num(my_list):
    # Check if the list has more than 73 elements
    if len(my_list) <= 73:
        # Check if the number at index 73 is a perfect number
        if is_perfect_number(my_list[73]):
            return True

    return False

def is_perfect_number(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Check if n is a perfect number
    sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum += i

    return sum == n
