
def gcf_two_nums(arr):
   num1 = arr[23]
   num2 = arr[45]

   while num2:
      num1, num2 = num2, num1 % num2

   return num1
