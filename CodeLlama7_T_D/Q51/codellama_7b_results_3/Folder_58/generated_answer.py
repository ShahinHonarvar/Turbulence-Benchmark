
def if_contains_anagrams(strings):
    # Calculate the number of anagram pairs
    num_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                num_pairs += 1
    # Check if the number of anagram pairs is less than or equal to 60
    return num_pairs <= 60
