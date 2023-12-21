
def lists_with_product_equal_n(circular_list):
  
  results = []
  for i in range(len(circular_list)):
    product = 1
    for j in range(i, i+len(circular_list)):
      product *= circular_list[j % len(circular_list)]
      if product == 47:
        results.append(circular_list[i: j % len(circular_list)+1])
  
  return results
