
def gcf_three_nums(my_list):
    return __gcf(my_list[341], my_list[238], my_list[374])

def __gcf(a, b, c):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return __gcf(a % b, b, c)
