
def palindrome_of_length_at_least_n(s):
   import re
   s = re.sub(r'\W+', '', s).lower()
   length = len(s)
   palindromes = set()
   for i in range(length):
       for j in range(i + 53, length + 1):
           substr = s[i:j]
           if substr == substr[::-1]:
               palindromes.add(substr)
   return palindromes
