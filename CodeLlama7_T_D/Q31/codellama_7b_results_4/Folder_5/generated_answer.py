
def if_perfect_num(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers.")
    # Check if the integer at index 67 is a perfect number
    if my_list[67] == find_perfect_number(my_list[67])):
        return True
    else:
        return False

def find_perfect_number(n):
    # Find the sum of the divisors of n (excluding n itself)
    sum_of_divisors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i * i != n:
                sum_of_divisors += n / i
    # Check if the sum of the divisors is equal to n
    if sum_of_divisors == n:
        return True
    else:
        return False
