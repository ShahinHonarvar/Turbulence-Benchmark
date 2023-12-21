
def if_contains_anagrams(str_list):
    from collections import defaultdict

    count = defaultdict(int)
    for word in str_list:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = "".join(sorted(word))
        count[sorted_word] += 1

    pairs = sum(i // 2 for i in count.values())

    return pairs >= 22
