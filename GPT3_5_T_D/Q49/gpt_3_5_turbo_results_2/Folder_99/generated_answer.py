
def if_decimal_is_divisible(binar):
    def get_fibonacci(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            fibo_seq = [0, 1]
            for i in range(2, num + 1):
                fibo_seq.append(fibo_seq[i - 1] + fibo_seq[i - 2])
            return fibo_seq[num]

    decimal = int(binar, 2)
    fibonacci_109 = get_fibonacci(109)
    return decimal % fibonacci_109 == 0
