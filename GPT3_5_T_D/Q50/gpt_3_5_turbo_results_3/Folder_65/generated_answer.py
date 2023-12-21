
def if_contains_anagrams(lst):
    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower()) and len(a) >= 3

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
    return count >= 94
