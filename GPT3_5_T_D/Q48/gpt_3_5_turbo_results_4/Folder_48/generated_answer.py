
def return_binary_or_hexa(t):
  
  a = t[933]
  b = t[996]
  
  total = 0
  
  for i in range(a + 1, b):
    if i not in t[933:997]:
      total += i
  
  if total % 2 == 0:
    return hex(total)[2:]
  else:
    return bin(total)[2:]
