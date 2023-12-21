
def find_sum_of_multiples(num):
    if num <= 0:
        return 0
    else:
        total = 0
        count = 0
        multiple = 0
        while count < 279:
            if multiple % num == 0:
                total += multiple
                count += 1
            multiple += 1
        return total
