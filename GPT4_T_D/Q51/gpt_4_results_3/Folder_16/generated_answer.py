
def if_contains_anagrams(str_list):
    def count_anagrams(str_list):
        from collections import Counter
        cnt = Counter(["".join(sorted(word.lower())) for word in str_list])
        pair_cnt = sum([v*(v-1)//2 for v in cnt.values()])
        return pair_cnt

    pair_cnt = count_anagrams([word for word in str_list if len(word)>=3])
    return pair_cnt <= 24
