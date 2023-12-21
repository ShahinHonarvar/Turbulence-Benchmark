
def if_contains_anagrams(list_of_strings):
    from collections import Counter

    def is_anagram(str1,str2):
        return Counter(str1.lower()) == Counter(str2.lower())

    pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i+1,len(list_of_strings)):
            if len(list_of_strings[i])>=3 and len(list_of_strings[j])>=3 and is_anagram(list_of_strings[i],list_of_strings[j]):
                pairs += 1
                if pairs > 41:
                    return False
    return True
