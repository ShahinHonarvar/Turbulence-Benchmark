def if_contains_anagrams(texts):
    anagrams_count = 0
    for first in texts:
        for second in texts:
            if len(first) >= 3 and len(second) >= 3 and first == second[::-1]:
                anagrams_count += 1
    return anagrams_count >= 7
