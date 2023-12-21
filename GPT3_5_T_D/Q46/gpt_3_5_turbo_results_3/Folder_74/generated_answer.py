
def gcf_three_nums(lst):
   def gcd(a, b):
      while b:
          a, b = b, a % b
      return a

   a = lst[99]
   b = lst[95]
   c = lst[80]

   gcf = gcd(a, gcd(b, c))
   return gcf
