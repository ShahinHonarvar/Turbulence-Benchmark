
def if_perfect_num(my_list):
    # Check if the index is valid
    if len(my_list) - 1 < 92:
        return False

    # Calculate the sum of the proper divisors
    def sum_divisors(n):
        sum = 0
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                sum += i

        return sum + 1

    # Check if the number is a perfect number
    perfect_num = my_list[92]
    if perfect_num == sum_divisors(perfect_num):
        return True

    else:

        return False
