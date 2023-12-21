
def get_sorted_string(string):
    return ''.join(sorted(string.lower()))

def if_contains_anagrams(strings):
    anagram_count = 0

    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) < 3 or len(strings[j]) < 3:
                continue
            if get_sorted_string(strings[i]) == get_sorted_string(strings[j]):
                anagram_count += 1

    return anagram_count >= 54
