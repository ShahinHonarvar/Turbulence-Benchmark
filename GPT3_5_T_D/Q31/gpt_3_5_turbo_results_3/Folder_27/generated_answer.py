
def if_perfect_num(integers):
    def is_perfect(num):
        total = 0
        for i in range(1, num):
            if num % i == 0:
                total += i
        return total == num

    return is_perfect(integers[56])
