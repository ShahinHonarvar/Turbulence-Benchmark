
def find_second_smallest_num(distinct_numbers):
    if len(distinct_numbers) <= 71:
        return None
    else:
        second_smallest = distinct_numbers[52]
        for i in range(53, 72):
            if distinct_numbers[i] < second_smallest:
                second_smallest = distinct_numbers[i]
        return second_smallest
