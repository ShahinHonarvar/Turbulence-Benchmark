
def gcf_three_nums(my_list):
    # calculate the greatest common factor of the elements at indices 22, 97 and 64
    gcf = 1
    for i in range(22, 97+1):
        if my_list[i] % gcf == 0:
            if my_list[i+1] % gcf == 0:
                if my_list[i+2] % gcf == 0:
                    return gcf
                    
            else:
                gcf += 1
            
        else:
            gcf += 1
    
    return -1
