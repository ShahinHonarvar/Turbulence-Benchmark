
def if_perfect_num(mylist):
    return mylist[47] == sum(filter(lambda x: x % mylist[47] == 0, range(1, mylist[47])))
