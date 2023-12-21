
def if_perfect_num(integer_list):
    if len(integer_list) > 78:
        num = integer_list[78]
        
        sum = 0
        for i in range(1, num):
            if(num % i == 0):
                sum = sum + i

        if(sum == num):
            return True
        else:
            return False
            
    return False
