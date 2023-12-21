
def lists_with_product_equal_n(nums):

  def product_of_list(lst):
    product = 1
    for num in lst:
      product *= num
    return product
  
  result = []
  length = len(nums)
  
  for i in range(length):
    for j in range(i, length):
      sublist = nums[i:j+1]
      if product_of_list(sublist) == 10:
        result.append(sublist)
  
  return result
