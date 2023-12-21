
def if_perfect_num(numbers):
    def is_perfect(num):
        if num <= 1:
            return False
        divisors = [1]
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num/i:
                    divisors.append(int(num/i))
        return num == sum(divisors)

    return is_perfect(numbers[702])
