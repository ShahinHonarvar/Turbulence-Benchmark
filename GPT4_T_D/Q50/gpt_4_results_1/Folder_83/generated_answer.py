
def if_contains_anagrams(lst):
    from collections import defaultdict

    sorted_word_list = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            sorted_word_list[sorted_word].append(word)

    pair_count = sum(len(words)*(len(words)-1)//2 for words in sorted_word_list.values())
    
    return pair_count >= 48
