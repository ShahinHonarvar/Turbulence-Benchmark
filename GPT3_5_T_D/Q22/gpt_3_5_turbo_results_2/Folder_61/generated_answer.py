
def find_sum_of_multiples(num):
    multiples = []
    count = 0
    current_num = num

    while count < 5:
        if current_num % num == 0:
            multiples.append(current_num)
            count += 1
        current_num += 1

    return sum(multiples)
