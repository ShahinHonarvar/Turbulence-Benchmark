
def if_contains_anagrams(word_list):
    # Check if the list contains at most 366 pairs of anagrams
    count = 0
    for i in range(len(word_list) - 1):
        for j in range(i + 1, len(word_list)):
            if sorted(word_list[i]) == sorted(word_list[j]):
                count += 1
                if count > 366:
                    return False

    return True
