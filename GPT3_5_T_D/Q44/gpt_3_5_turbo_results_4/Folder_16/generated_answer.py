

def composite_nums_between_indices(numbers):
    composites = set()
    
    for index in range(40, 81):
        num = numbers[index]
        
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    composites.add(num)
                    break
    
    return composites
