
def if_contains_anagrams(string_list):
    # Count the number of anagrams in the list
    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list))):
            if sorted(string_list[i]) == sorted(string_list[j]):
                anagram_count += 1
                # If there are at least 20 pairs of anagrams in the list, return True
                if anagram_count >= 20:
                    return True
            else:
                continue

    # If there are no anagrams in the list, return False

    return False
