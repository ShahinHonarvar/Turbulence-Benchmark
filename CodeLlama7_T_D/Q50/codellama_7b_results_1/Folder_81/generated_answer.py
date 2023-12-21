
def if_contains_anagrams(words):
  # Create a dictionary to store the anagram counts
  anagram_counts = {}

  for word in words:
    # Get the length of the word
    word_length = len(word)

    # If the word is at least three characters long, continue
    if word_length >= 3:
      # Create a lowercase version of the word
      lowercase_word = word.lower()

      # If the anagram count for this length has not been initialized yet, do so now
      if lowercase_word not in anagram_counts:
        anagram_counts[lowercase_word] = 0

      # Increment the anagram count for this length
      anagram_counts[lowercase_word] += 1

  # Check if there are at least 16 pairs of anagrams in the given list
  return sum(anagram_counts.values()) >= 16
