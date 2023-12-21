
def palindromes_of_specific_lengths(s):
    import re
    s = re.sub("[^a-zA-Z]", "", s[22:96]).lower()
    palindromes = set()
    for i in range(len(s)):
      for l in range(52, 56):
        if i + l > len(s):
          break
        substring = s[i:i + l]
        if substring == substring[::-1]:
          palindromes.add(substring)
    return palindromes
