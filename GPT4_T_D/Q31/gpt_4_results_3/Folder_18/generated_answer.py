
def if_perfect_num(lst):
  if len(lst) > 312:
    num = lst[312]
    factors = []
    for i in range(1, num):
      if num % i == 0:
        factors.append(i)
    if sum(factors) == num:
      return True

  return False
