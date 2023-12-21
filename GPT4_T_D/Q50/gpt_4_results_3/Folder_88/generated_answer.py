
def if_contains_anagrams(lst):
    from collections import defaultdict
  
    word_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            word_dict[''.join(sorted(word.lower()))].append(word)

    pairs = sum([len(words)*(len(words)-1)//2 for words in word_dict.values()])

    return pairs >= 34
