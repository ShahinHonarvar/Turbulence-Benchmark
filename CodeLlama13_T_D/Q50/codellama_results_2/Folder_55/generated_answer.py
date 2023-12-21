
def if_contains_anagrams(mylist):
    anagram_pairs = 0
    for i in range(len(mylist)):
        for j in range(i+1, len(mylist)):
            if is_anagram(mylist[i], mylist[j]):
                anagram_pairs += 1
                if anagram_pairs == 15:
                    return True
    return False

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())
