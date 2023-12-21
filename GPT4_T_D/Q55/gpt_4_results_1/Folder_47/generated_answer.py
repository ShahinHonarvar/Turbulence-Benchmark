
def lists_with_product_equal_n(numbers):
    size = len(numbers)
    answer = []
    
    for start in range(size):
        for end in range(start, start + size):
            sublist = numbers[start:end] if end <= size else numbers[start:] + numbers[:end%size]
            product = 1
            for num in sublist:
                product *= num
            if product == -94:
                if sublist not in answer:
                    answer.append(sublist)
    return answer
