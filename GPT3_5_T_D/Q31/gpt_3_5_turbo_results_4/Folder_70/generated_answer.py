
def if_perfect_num(lst):
    def is_perfect_num(num):
        total = 0
        for i in range(1, num):
            if num % i == 0:
                total += i
        return total == num

    return is_perfect_num(lst[845])
