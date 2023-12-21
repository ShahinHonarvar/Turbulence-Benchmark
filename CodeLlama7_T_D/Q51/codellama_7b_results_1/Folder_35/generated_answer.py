
def if_contains_anagrams(words):
    # Check if there are at most 210 pairs of anagrams in the given list
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                count += 1
                if count > 210:
                    return False

    # If there are no more than 210 pairs of anagrams in the given list, return True
    return True
