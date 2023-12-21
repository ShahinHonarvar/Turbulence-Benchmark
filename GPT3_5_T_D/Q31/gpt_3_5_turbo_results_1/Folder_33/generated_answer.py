
def if_perfect_num(numbers):
    def is_perfect(num):
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        return sum(factors) == num
    
    if len(numbers) >= 322:
        return is_perfect(numbers[321])
    else:
        return False
