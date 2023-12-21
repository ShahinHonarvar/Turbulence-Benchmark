
def sum_in_range(list_of_integers):
    sum_result = 0
    for i in list_of_integers:
        if -3 <= i <= 6:
            sum_result += i
    return sum_result
