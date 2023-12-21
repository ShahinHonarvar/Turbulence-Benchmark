
def if_perfect_num(integer_list):
    def is_perfect_num(num):
        if num <= 0:
            return False
        divisor_sum = sum(i for i in range(1, num) if num % i == 0)
        return divisor_sum == num

    return is_perfect_num(integer_list[96])
