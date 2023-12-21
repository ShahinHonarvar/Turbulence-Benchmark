
def composite_nums_between_indices(num_list):
    composite_nums = set()
    
    for i in range(60, min(201,len(num_list))):
        num = num_list[i]
        if num > 1:
            for potential_factor in range(2,int(num**0.5)+1):
                if num % potential_factor == 0:
                    composite_nums.add(num)
                    break

    return composite_nums
