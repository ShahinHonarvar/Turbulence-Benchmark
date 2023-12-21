
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    for word in my_list:
        # Get the anagram of the current word
        anagram = ''.join(sorted(word.lower()))

        if len(anagram) < 3:
            continue

        # Increment the count of the anagram
        if anagram in anagram_counts:
            anagram_counts[anagram] += 1

        else:
            anagram_counts[anagram] = 1

    # Check if there are more than 188 pairs of anagrams in the list
    return sum(count > 1 for count in anagram_counts.values()) <= 188
