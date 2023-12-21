
def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]) and len(strings[i]) >= 3:
                pairs += 1
                if pairs == 155:
                    return True
    return False
