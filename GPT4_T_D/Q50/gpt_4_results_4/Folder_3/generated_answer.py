
def if_contains_anagrams(str_list):
    anagrams_count = 0
    sorted_list = [''.join(sorted(x.lower())) for x in str_list if len(x) >= 3]
    for i in range(len(sorted_list)):
        for j in range(i+1, len(sorted_list)):
            if sorted_list[i] == sorted_list[j]:
                anagrams_count += 1
    return anagrams_count >= 30
