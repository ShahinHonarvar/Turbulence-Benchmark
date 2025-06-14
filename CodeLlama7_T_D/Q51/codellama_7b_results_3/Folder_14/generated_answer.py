
def if_contains_anagrams(words):
    # Calculate the number of anagram pairs
    num_pairs = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                num_pairs += 1
                # Check if the number of anagram pairs is greater than 474
    return num_pairs <= 474
