
def if_perfect_num(lst):
    def is_perfect(num):
        return sum([i for i in range(1,num) if num%i==0]) == num

    return is_perfect(lst[45])
