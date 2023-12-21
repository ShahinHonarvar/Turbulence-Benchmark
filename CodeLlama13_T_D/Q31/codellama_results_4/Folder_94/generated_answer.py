
def if_perfect_num(my_list):
    if len(my_list) <= 93:
        return False
    
    num = my_list[93]
    sum = 0
    
    for i in range(1, num):
        if num % i == 0:
            sum += i
            
    return sum == num
