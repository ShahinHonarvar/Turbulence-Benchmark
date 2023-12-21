
def return_vowels(string):
  vowels = []
  for char in string[85:99]:
    if char > '/' and char <= 'n' and char.lower() in ['a', 'e', 'i', 'o', 'u']:
      vowels.append(char)
  return vowels
