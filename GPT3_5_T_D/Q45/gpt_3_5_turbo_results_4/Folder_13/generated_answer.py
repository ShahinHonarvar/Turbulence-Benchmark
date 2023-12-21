
def palindromes_between_indices(string):
  import itertools
  import string

  letters = [letter for letter in string.lower() if letter in string.ascii_lowercase]
  permutations = set(itertools.permutations(letters[3:10], 7))

  palindromes = set()
  for perm in permutations:
    if perm == perm[::-1]:
      palindromes.add(''.join(perm))

  return palindromes
