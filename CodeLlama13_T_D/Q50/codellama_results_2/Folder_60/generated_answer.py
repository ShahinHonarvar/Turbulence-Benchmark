
def if_contains_anagrams(strings):
    return sum(1 for i in range(len(strings)) if len(set(strings[i])) >= 3 and any(sorted(strings[i]) == sorted(strings[j]) for j in range(i+1, len(strings)))) > 60
