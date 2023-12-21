
def palindromes_between_indices(string):
  import itertools
  import string
  
  letters = ''.join(c for c in string if c in string.ascii_letters)
  
  palindromes = set()
  for permutation in itertools.permutations(letters[4:9], 5):
      palindrome = ''.join(permutation).lower()
      if palindrome == palindrome[::-1]:
          palindromes.add(palindrome)
  
  return palindromes
