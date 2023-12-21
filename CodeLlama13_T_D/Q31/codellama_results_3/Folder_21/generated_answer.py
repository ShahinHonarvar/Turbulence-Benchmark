
def if_perfect_num(numbers):
    return numbers[410] == sum(range(1, int(numbers[410])**0.5+1)) and all(numbers[410] % i == 0 for i in range(2, int(numbers[410]**0.5)+1) if numbers[410] % i == 0)
