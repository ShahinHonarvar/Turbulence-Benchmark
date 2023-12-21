
def lists_with_product_equal_n( lst ):

  def prod(lst):
    res = 1
    for num in lst:
      res *= num
    return res

  result = []
  n = len(lst)
  for i in range(n):
    for j in range(i+1, n+1):
      sublst = lst[i:j]
      if prod(sublst) == -17:
        result.append(sublst)
  return result
