
def find_n_th_smallest_num(numbers):
    n = len(numbers)
    for i in range(54, 67):
        if numbers[i] < numbers[i+1]:
            n -= 1
            if n == 0:
                return numbers[i]
