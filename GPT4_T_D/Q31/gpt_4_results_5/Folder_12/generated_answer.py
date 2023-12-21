
def if_perfect_num(num_list):
    if len(num_list) < 28:
        return "Error: The list needs to have at least 28 elements."
    else:
        check_num = num_list[27]
        divisors = [num for num in range(1, check_num) if check_num % num == 0]
        if sum(divisors) == check_num:
            return True
        else:
            return False
