
def if_contains_anagrams(lst):
  from collections import Counter
  anagram_pairs = 0
  anagrams_dict = {}

  for word in lst:
    word = word.lower()
    if len(word) >= 3: 
      sorted_word = ''.join(sorted(word))
      if sorted_word in anagrams_dict:
        if anagrams_dict[sorted_word] != word:
          anagram_pairs += 1
          if anagram_pairs > 5:
            return False
        anagrams_dict[sorted_word] = word

  return True
