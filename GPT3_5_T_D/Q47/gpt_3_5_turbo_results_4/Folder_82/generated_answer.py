
import string

def palindromes_of_specific_lengths(string):
   palindromes = set()
   string = string.lower()[3:301]
   for length in range(30, 301):
       for i in range(len(string) - length + 1):
           substring = string[i:i+length]
           if substring == substring[::-1] and all(char in string.ascii_letters for char in substring):
               palindromes.add(substring)
   return palindromes
