
def lists_with_product_equal_n(numbers):
    sublists = []
    size = len(numbers)

    for i in range(size):
        product = 1
        sublist = []
        
        for j in range(i, i + size):
            index = j % size
            number = numbers[index]
            product *= number
            sublist.append(number)
            
            if product == 18:
                sublists.append(sublist[:])
                break
                
            elif product > 18:
                break
    
    return sublists
