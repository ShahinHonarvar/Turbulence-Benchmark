

def composite_nums_between_indices(numbers):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return True
        return False
            
    index_range = numbers[20:201]
    composites = {x for x in index_range if is_composite(x)}
    return composites
