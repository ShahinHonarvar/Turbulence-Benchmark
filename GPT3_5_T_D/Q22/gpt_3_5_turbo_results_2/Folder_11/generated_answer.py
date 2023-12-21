
def find_sum_of_multiples(n):
    sum = 0
    count = 0
    num = n
  
    while count < 56:
        if is_multiple(num, n):
            sum += num
            count += 1
        num += n
  
    return sum

def is_multiple(x, n):
    return x % n == 0
