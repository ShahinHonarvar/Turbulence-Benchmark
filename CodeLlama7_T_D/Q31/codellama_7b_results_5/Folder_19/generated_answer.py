
def if_perfect_num(my_list):
    # Check if the input is a list of positive integers
    if not (isinstance(my_list, list) and all(isinstance(x, int) and x > 0 for x in my_list))):
        raise ValueError("The input must be a list of positive integers.")
    # Check if the integer at index 13 is a perfect number
    if my_list[13] == find_perfect_number(my_list[13])):
        return True
    else:
        return False

def find_perfect_number(n):
    # Find the sum of the divisors of n
    divisors = [i for i in range(1, int(n ** 0.5) + 1) if n % i == 0]
    sum_divisors = sum(divisors)
    # Check if the sum of the divisors is equal to n
    if sum_divisors == n:
        return True
    else:
        return False
