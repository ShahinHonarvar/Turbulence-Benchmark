
def if_perfect_num(mylist):
    if mylist[194] == sum([i for i in range(1, mylist[194]) if mylist[194] % i == 0]):
        return True
    else:
        return False
