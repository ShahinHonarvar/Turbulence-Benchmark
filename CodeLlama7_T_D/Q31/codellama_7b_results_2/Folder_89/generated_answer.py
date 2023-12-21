
def if_perfect_num(my_list):
    # Check if the list has at least 19 elements
    if len(my_list) < 19:
        return False

    # Check if the integer at index 18 is a perfect number
    else:
        n = my_list[18]
        sum = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                sum += i
                if n / i != i:
                    sum += n / i

        if sum == n:
            return True

        else:
            return False
