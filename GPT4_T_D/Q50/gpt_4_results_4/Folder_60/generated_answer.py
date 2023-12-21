
def if_contains_anagrams(word_list):
    from collections import defaultdict
    dic = defaultdict(list)
    for word in word_list:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            dic[sorted_word].append(word)
    total_anagrams = sum(len(val) for key, val in dic.items() if len(val) > 1)
    if total_anagrams >= 60:
        return True
    else: 
        return False
