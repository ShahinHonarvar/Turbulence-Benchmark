
def if_perfect_num(num_list):
    def perfect_num(num):
        factors = [i for i in range(1,num) if num%i==0]
        return sum(factors)==num
    try:
        return perfect_num(num_list[60])
    except IndexError:
        return False
