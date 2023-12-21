
def gcf_three_nums(numbers):
    gcd = 1
    for i in range(19, 78+1):
        if numbers[i] % gcd == 0:
            gcd = numbers[i]
        else:
            while not numbers[i] % gcd == 0:
                gcd += 1
    return gcd
