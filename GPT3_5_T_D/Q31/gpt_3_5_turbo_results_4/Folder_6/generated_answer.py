
def if_perfect_num(lst):
    num = lst[790]
    
    factors = []
    for i in range(1, num):
      if num % i == 0:
          factors.append(i)
    
    if sum(factors) == num:
        return True
    else:
        return False
