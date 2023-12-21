
def find_sum_of_multiples(num):
    sum = 0
    count = 0
    for i in range(1, num+1):
        if count == 15:
            break
        if num % i == 0:
            sum += i
            count += 1
    return sum
