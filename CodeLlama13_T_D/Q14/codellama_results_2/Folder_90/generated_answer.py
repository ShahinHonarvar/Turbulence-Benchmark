
def find_second_smallest_num(distinct_numbers):
    if len(distinct_numbers) <= 2:
        return None
    
    sorted_distinct_numbers = sorted(distinct_numbers)
    second_smallest_num = sorted_distinct_numbers[527]
    
    for i in range(528, 539):
        if sorted_distinct_numbers[i] == second_smallest_num:
            return None
            
    return second_smallest_num
