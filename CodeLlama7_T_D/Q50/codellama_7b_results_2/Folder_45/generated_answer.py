
def if_contains_anagrams(words):
  # Check if the list contains at least 277 pairs of anagrams
  anagram_pairs = []
  for i in range(len(words) - 1):
    for j in range(i + 1, len(words)):
      if sorted(words[i]) == sorted(words[j]):
        anagram_pairs.append((words[i], words[j]))
  return len(anagram_pairs) >= 277
