from typing import List

#(1) A python function that returns the list of all integers from {H0,t:int} to {H1,t:int} both inclusive.
def all_ints_inclusive(H0: int, H1: int) -> List[int]:
    return [i for i in range(H0, H1 + 1) if H0 <= H1]


#(2) A python function that returns the list of all integers from {H0,t:int} to {H1,t:int} both exclusive.
def all_ints_exclusive(H0: int, H1: int) -> List[int]:
    return [i for i in range(H0 + 1, H1) if H0 < H1]


#(3) A python function that returns the list of all positive integers from {H0,t:int} to {H1,t:int} both inclusive.
def all_pos_ints_inclusive(H0: int, H1: int) -> List[int]:
    return [i for i in range(H0, H1 + 1) if H0 <= H1 and i > 0]


#(4) A python function that returns the list of all positive integers from {H0,t:int} to {H1,t:int} both exclusive.
def all_pos_ints_exclusive(H0: int, H1: int) -> List[int]:
    return [i for i in range(H0 + 1, H1) if H0 < H1 and i > 0]


#(5) A python function that returns the list of all negative integers from {H0,t:int} to {H1,t:int} both inclusive.
def all_neg_ints_inclusive(H0: int, H1: int) -> List[int]:
    return [i for i in range(H0, H1 + 1) if H0 <= H1 and i < 0]


#(6) A python function that returns the list of all negative integers from {H0,t:int} to {H1,t:int} both exclusive.
def all_neg_ints_exclusive(H0: int, H1: int) -> List[int]:
    return [i for i in range(H0 + 1, H1) if H0 < H1 and i < 0]


#(7) A python function that returns the list of all even integers from {H0,t:int} to {H1,t:int} both inclusive.
def all_even_ints_inclusive(H0: int, H1: int) -> List[int]:
    return [i for i in range(H0, H1 + 1) if H0 <= H1 and i % 2 == 0]


#(8) A python function that returns the list of all even integers from {H0,t:int} to {H1,t:int} both exclusive.
def all_even_ints_exclusive(H0: int, H1: int) -> List[int]:
    return [i for i in range(H0 + 1, H1) if H0 < H1 and i % 2 == 0]


#(9) A python function that returns the list of all odd integers from {H0,t:int} to {H1,t:int} both inclusive.
def all_odd_ints_inclusive(H0: int, H1: int) -> List[int]:
    return [i for i in range(H0, H1 + 1) if H0 <= H1 and i % 2 != 0]


#(10) A python function that returns the list of all odd integers from {H0,t:int} to {H1,t:int} both exclusive.
def all_odd_ints_exclusive(H0: int, H1: int) -> List[int]:
    return [i for i in range(H0 + 1, H1) if H0 < H1 and i % 2 != 0]


#(11) A python function takes {H0,s:list,t:obj} as input. It should return the largest element of {H0,s:list,t:obj}.
def largest_element(H0: List[object]) -> object:
    if not H0:
        return None

    return max(H0)


#(12) A python function takes {H0,s:list,t:obj} as input. It should return the second largest element of the {H0,s:list,t:obj}.
# For example if [0,1,2,2] is the input then the function should return 2.
def second_largest_element(H0: List[object]) -> object:
    if len(H0) <= 1:
        return None
    H0.sort()

    return H0[-2]


#(13) A python function that returns the list of all integers from {H0,t:int} to {H1,t:int} inclusive that are divisible by {H2,t:int}.
def all_ints_div_by_n_inclusive(H0: int, H1: int, H2: int) -> List[int]:
    return [i for i in range(H0, H1 + 1) if H0 <= H1 and i % H2 == 0]


#(14) A python function that returns the list of all integers from {H0,t:int} to {H1,t:int} exclusive that are divisible by {H2,t:int}.
def all_ints_div_by_n_exclusive(H0: int, H1: int, H2: int) -> List[int]:
    return [i for i in range(H0 + 1, H1) if H0 < H1 and i % H2 == 0]


#(15) A python function that returns the list of all integers from {H0,t:int} to {H1,t:int} inclusive that are not divisible by {H2,t:int}.
def all_ints_not_div_by_n_inclusive(H0: int, H1: int, H2: int) -> List[int]:
    return [i for i in range(H0, H1 + 1) if H0 <= H1 and i % H2 != 0]


#(16) A python function takes {H0,s:list,t:obj} and {H1,t:int} as inputs. It should return the {H1,t:int}-th largest element of {H0,s:list,t:obj}.
# For example if [7,7,0,1,0,1,5] and 4 are the inputs, then the function should return 1.
def nth_largest_element(H0: List[object], H1: int) -> object:
    if len(H0) < H1 or H1 <= 0:
        return None
    H0.sort()

    return H0[-H1]


#(17) A python function that takes {H0,s:list,t:obj} as input. It should return the smallest element of {H0,s:list,t:obj}.
def smallest_element(H0: List[object]) -> object:
    if not H0:
        return None

    return min(H0)


#(18) A python function takes {H0,s:list,t:obj} as input. It should return the second smallest element of {H0,s:list,t:obj}.
# For example if the input is [2,0,1,0,1], then the function should return 0.
def second_smallest_element(H0: List[object]) -> object:
    if len(H0) <= 1:
        return None
    H0.sort()

    return H0[1]


#(19) A python function takes {H0,s:list,t:obj} and {H1,t:int} as input. It should return the {H1,t:int}-th smallest element of {H0,s:list,t:obj}.
# For example if the inputs are [7,7,0,1,0,1,5] and 4 then the function should return 1.
def nth_smallest_element(H0: List[object], H1: int) -> object:
    if len(H0) < H1 or H1 <= 0:
        return None
    H0.sort()

    return H0[H1 - 1]


#(20) A python function that returns the list of all integers from {H0,t:int} to {H1,t:int} inclusive that are divisible by {H2,t:int} and H3_int.
def all_ints_div_by_m_n_inclusive(H0: int, H1: int, H2: int, H3: int) -> List[int]:
    return [i for i in range(H0, H1 + 1) if H0 <= H1 and i % H2 == 0 and i % H3 == 0]


#(21) A python function that returns the list of all integers from {H0,t:int} to {H1,t:int} inclusive that are divisible by {H2,t:int} or H3_int.
def all_ints_div_by_m_n_exclusive(H0: int, H1: int, H2: int, H3: int) -> List[int]:
    return [i for i in range(H0, H1 + 1) if H0 <= H1 and i % H2 == 0 or i % H3 == 0]


#(22) A python function that returns the sum of all integers from from {H0,t:int} to {H1,t:int} inclusive.
def sum_ints(H0: int, H1: int) -> int:
    return sum(range(H0, H1 + 1))


#(23) A python function that returns the sum of all even integers from {H0,t:int} to {H1,t:int} inclusive.
def sum_even_ints(H0: int, H1: int) -> int:
    return sum([i for i in range(H0, H1 + 1) if i % 2 == 0])


#(24) A python function that returns the sum of all odd integers from {H0,t:int} to {H1,t:int} inclusive.
def sum_odd_ints(H0: int, H1: int) -> int:
    return sum([i for i in range(H0, H1 + 1) if i % 2 != 0])


#(25) A python function that returns the sum of all integers from {H0,t:int} to {H1,t:int} inclusive that are divisible by {H2,t:int}.
def sum_ints_div_by_n(H0: int, H1: int, H2: int) -> int:
    return sum([i for i in range(H0, H1 + 1) if i % H2 == 0])


#(26) A python function that takes {H0,t:int} and returns the list of all positive divisors of {H0,t:int}.
def all_divs(H0: int) -> List[int]:
    result = []
    if H0 <= 0:
        return result
    return [i for i in range(1, H0 + 1) if H0 % i == 0]


#(27) A python function that takes {H0,t:int} and returns the sum of all positive divisors of {H0,t:int}.
def sum_all_divs(H0: int) -> int:
    result = []
    if H0 <= 0:
        return sum(result)
    return sum([i for i in range(1, H0 + 1) if H0 % i == 0])


#(28) A python function takes {H0,t:int} and {H1,t:int} and H2_list_int as inputs. The function should return the sum of all elements from the given list that lie in the range {H0,t:int} to {H1,t:int} inclusive.
def sum_in_range(H2, H0, H1):
    if not H2 or H0 >= H1:
        return None

    result = 0
    for i in H2:
        if H0 <= i <= H1:
            result += i

    return result


#(29) A python function takes {H0,t:int} as input. It should return the list of all prime numbers up to {H0,t:int} inclusive.
def prime_nums(H0: int) -> List[int]:
    result = []
    if H0 <= 1:
        return result
    else:
        flag = False
        for i in range(2, H0 + 1):
            for j in range(2, i):
                if i % j == 0:
                    flag = True
                    break
            if flag:
                flag = False
            else:
                result.append(i)
        return result


#(30) A python function takes {H0,t:int} as input. It should return the sum of all prime numbers up to {H0,t:int} inclusive.
def sum_prime_nums(H0: int) -> int:
    result = []
    if H0 <= 1:
        return sum(result)
    else:
        flag = False
        for i in range(2, H0 + 1):
            for j in range(2, i):
                if i % j == 0:
                    flag = True
                    break
            if flag:
                flag = False
            else:
                result.append(i)
        return sum(result)


#(31) A python function takes {H0,t:int} and {H1,t:int} as inputs. It should return the list of all prime numbers between {H0,t:int} and {H1,t:int} inclusive.
def prime_nums_x_y(H0: int, H1: int) -> List[int]:
    result = []
    if H0 > H1:
        return result
    elif H0 <= 1 and H1 <= 1:
        return result
    elif H0 <= 1:
        return prime_nums_x_y(2, H1)
    else:
        flag = False
        for i in range(H0, H1 + 1):
            for j in range(2, i):
                if i % j == 0:
                    flag = True
                    break
            if flag:
                flag = False
            else:
                result.append(i)
        return result


#(32) A python function takes {H0,t:int} and {H1,t:int} as inputs. It should return the sum of all prime numbers between {H0,t:int} and {H1,t:int} inclusive.
def sum_prime_nums_x_y(H0: int, H1: int) -> int:
    result = []
    if H0 > H1:
        return sum(result)
    elif H0 <= 1 and H1 <= 1:
        return sum(result)
    elif H0 <= 1:
        return sum_prime_nums_x_y(2, H1)
    else:
        flag = False
        for i in range(H0, H1 + 1):
            for j in range(2, i):
                if i % j == 0:
                    flag = True
                    break
            if flag:
                flag = False
            else:
                result.append(i)
        return sum(result)


#(33) A python function takes {H0,t:int} as input. It should return a list of all composite numbers up to {H0,t:int} inclusive.
def find_composite_numbers(H0: int) -> List[int]:
    result = []
    if H0 < 4:
        return result
    else:
        for i in range(4, H0 + 1):
            for j in range(2, i):
                if i % j == 0:
                    result.append(i)
                    break
    return result


#(34) A python function takes {H0,t:int} and {H1,t:int} as inputs. It should returns a list of all composite numbers between {H0,t:int} and {H1,t:int} inclusive.
def find_composite_nums_x_y(H0: int, H1: int) -> List[int]:
    result = []
    if H0 > H1:
        return result
    if H0 < 4:
        H0 = 4
    for i in range(H0, H1 + 1):
        for j in range(2, i):
            if i % j == 0:
                result.append(i)
                break
    return result


#(35) A python function takes {H0,t:int} and {H1,t:int} as inputs. It should return the greatest common factor of {H0,t:int} and {H1,t:int}.
def gcf(H0: int, H1: int) -> int:
    result = None
    if H0 == 0 and H1 == 0:
        return result
    elif H0 < 0:
        return gcf(-H0, H1)
    elif H1 < 0:
        return gcf(H0, -H1)
    elif H0 == 0:
        return H1
    elif H1 == 0:
        return H0
    else:
        H0_factors = [i for i in range(1, H0 + 1) if H0 % i == 0]
        H1_factors = [i for i in range(1, H1 + 1) if H1 % i == 0]
        for i in reversed(H0_factors):
            if i in H1_factors:
                result = i
                break
        return result


#(36) A python function takes {H0,t:int}, {H1,t:int} and {H2,t:int} as inputs. It should return the greatest common factor of {H0,t:int} and {H1,t:int} and {H2,t:int}.
def gcf(H0: int, H1: int, H2: int) -> int:
    result = None
    if H0 == 0 and H1 == 0 and H2 == 0:
        return result
    elif H0 < 0:
        return gcf(-H0, H1, H2)
    elif H1 < 0:
        return gcf(H0, -H1, H2)
    elif H2 < 0:
        return gcf(H0, H1, -H2)
    else:
        if H0 == 0:
            H0_factors = [i for i in range(0, max(H1, H2) + 1)]
        else:
            H0_factors = [i for i in range(1, H0 + 1) if H0 % i == 0]
        if H1 == 0:
            H1_factors = [i for i in range(0, max(H0, H2) + 1)]
        else:
            H1_factors = [i for i in range(1, H1 + 1) if H1 % i == 0]
        if H2 == 0:
            H2_factors = [i for i in range(0, max(H0, H1) + 1)]
        else:
            H2_factors = [i for i in range(1, H2 + 1) if H2 % i == 0]

        for i in reversed(H0_factors):
            if i in H1_factors and i in H2_factors:
                result = i
                break
        return result


#(37) A python function takes {H0,t:int,r:>0} as input. It should return true if {H0,t:int,r:>0} is a perfect number otherwise it should return false.
def is_perfect_number(H0: int) -> bool:
    if H0 <= 0:
        return False
    return sum([i for i in range(1, H0) if H0 % i == 0]) == H0


#(38) A python function takes {H0,t:int,r:>0} as input. It should return the list of all perfect numbers up to {H0,t:int,r:>0} inclusive.
def all_perfect_numbers(H0: int) -> List[int]:
    result = []
    if H0 <= 0:
        return result
    for n in range(1, H0 + 1):
        if sum([i for i in range(1, n) if n % i == 0]) == n:
            result.append(n)
    return result


#(39) A python function takes {H0,s:list,t:obj} and H1_list_obj as inputs. The function should return a new list of all similar elements in {H0,s:list,t:obj} and H1_list_obj.
def similar_elements(H0: List[object], H1: List[object]) -> List[object]:
    result = []
    if not H0 or not H1:
        return result

    for i in H0:
        if i in H1 and i not in result:
            result.append(i)

    return result


#(40) A python function takes {H0,s:list,t:obj} as input. It should return the list of all sublists of {H0,s:list,t:obj}.
def all_sublists(H0: List[object]) -> List[List[object]]:
    from itertools import combinations

    result = []
    for i in range(0, len(H0) + 1):
        result += (list(combinations(H0, i)))

    return [list(i) for i in result]


#(41) A python function takes {H0,s:list,t:obj} and {H1,t:int} as inputs. It should return the list of all sublists of length {H1,t:int} of {H0,s:list,t:obj}.
def all_sublists_length_n(H0: List[object], H1: int) -> List[List[object]]:
    from itertools import combinations

    result = []
    if H1 > len(H0) or H1 < 0:
        return result
    result += (list(combinations(H0, H1)))

    return [list(i) for i in result]


#(42) A python function takes {H0,s:list,t:obj} and H1_list_obj as inputs. It should return true if either is a sublist of the other otherwise, it should return false.
def if_sublist(H0: List[object], H1: List[object]) -> bool:
    if H0 == [] or H1 == []:
        return True

    result1 = False
    result2 = False
    c1 = 0
    c2 = 0

    if len(H0) < len(H1):
        for i in H0:
            if i in H1:
                c1 += 1
        if len(H0) == c1:
            result1 = True

    else:
        for i in H1:
            if i in H0:
                c2 += 1
        if len(H1) == c2:
            result1 = True

    return result1 or result2


#(43) A Python function takes {H0,s:list,t:obj} as input. The function should return a list where all the elements of {H0,s:list,t:obj} are sublists of the returned list.
# For example, if the input is [[1], [2], [3]] then the function should return [1, 2, 3].
def original_list(H0: List[List[object]]) -> List[object]:
    import itertools

    return list(itertools.chain.from_iterable(H0))


#(44) A python function that takes {H0,s:list,t:obj} as input. The function should remove duplicates from {H0,s:list,t:obj} and returns the new list.
def remove_duplicate(H0: List[object]) -> List[object]:
    result = []
    if not H0:
        return result

    for i in H0:
        if i not in result:
            result.append(i)

    return result


#(45) A python functon takes {H0,s:list,t:float} as input. It should return the average of the numbers in {H0,s:list,t:float}.
def mean_of_list(H0: List[float]) -> float:
    return sum(H0) / len(H0)


#(46) A python functon takes {H0,s:list,t:float} as input. It should return the mode of the numbers in {H0,s:list,t:float}. If the given list has more than one mode then the function should return all of them.
def mode_of_list(H0: List[float]) -> List[float]:
    import operator

    result = []
    d = {num: H0.count(num) for num in H0}
    if all(v == 1 for v in d.values()):
        return result
    sorted_d = (dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True)))
    largest = list(sorted_d.values())[0]
    for k, v in sorted_d.items():
        if v == largest:
            result.append(k)

    return result


#(47) A python function takes {H0,t:str} as input. It should return the list of all characters of {H0,t:str}.
def string_chars(H0: str) -> List[str]:
    result = []
    if H0 == '':
        return result

    return [c for c in H0]


#(48) A python function takes {H0,t:str} as input. It should return the number of all vowels (both lower case and upper case) in {H0,t:str}.
def count_vowels(H0: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    H0 = H0.lower()
    for c in H0:
        if c in vowels:
            count += 1

    return count


#(49) A python function takes {H0,t:str,c:>2} and {H1,t:int} as inputs. The function should return the list of all palindrome sequences of size {H1,t:int} in {H0,t:str,c:>2}.
# For example, a palindrome sequence of size 4 in "Yesterday we met Anna" is "anna".
def find_all_palindrome_x(H0: str, H1: int) -> List[str]:
    if len(H0) <= 2 or H1 <= 2 or H1 > len(H0):
        return []

    H0 = H0.lower()
    H0 = H0.replace(" ", "")
    all_palindrome = []
    for i in range(0, len(H0)):
        chunk = H0[i:i + H1]
        if len(chunk) < H1:
            break
        if chunk == chunk[::-1]:
            all_palindrome.append(chunk)

    if len(all_palindrome) > 0:
        return all_palindrome
    else:
        return None


#(50) A python function takes {H0,t:str,c:>2} as input. The function should return the list of all palindrome sequences of size at least three in {H0,t:str,c:>2}.
# For example, if "Yesterday we met Anna" is given to the function, it should return ['eme', 'anna'].
def find_all_palindrome(H0: str) -> List[str]:
    if len(H0) <= 2:
        return []
    H0 = H0.lower()
    H0 = H0.replace(" ", "")
    c = 3
    all_palindrome = []
    for _ in range(0, len(H0) - 2):
        for i in range(0, len(H0)):
            chunk = H0[i:i + c]
            if len(chunk) < c:
                break
            if chunk == chunk[::-1]:
                all_palindrome.append(chunk)
        c += 1

    if len(all_palindrome) > 0:
        return all_palindrome
    else:
        return None


#(51) A python function takes {H0,s:list,t:char} and {H1,t:int} as inputs. The function should return the list of all possible palindrome sequences of length {H1,t:int} made out of only those characters.
# For example, if the function takes ['e','v','a','e'] it should return ['eve', 'eae'].
def all_palindrome_length_3(H0: List[str], H1: int) -> List[str]:
    from itertools import combinations

    result = []
    if len(H0) < H1 or H1 < 3 or len(H0) < 3:
        return result
    result += (list(combinations(H0, H1)))

    return [''.join(i) for i in result if i == i[::-1]]


#(52) A Python function takes {H0,s:list,t:char} as input. The function should return a list of all palindrome sequences that can be created using only characters in {H0,s:list,t:char}. All returned palindrome sequences must be at least three characters long.
# For example, if ['t', 'e', 's', 'e', 't'] is the input, the function should return ['tet', 'tst', 'tet', 'ese', 'teet', 'teset'].
def all_palindrome_all_length(H0: List[str]) -> List[str]:
    from itertools import combinations

    result = []
    if len(H0) < 3:
        return result
    for i in range(3, len(H0) + 1):
        result += (list(combinations(H0, i)))

    return [''.join(i) for i in result if i == i[::-1]]


#(53) A python function takes {H0,s:list,t:char} and {H1,t:int} as inputs. The function should return the list of all possible strings of length {H1,t:int} constructed from the characters in {H0,s:list,t:char}. Repeat characters are not allowed.
def permutations_no_repeat_length_x(H0: List[str], H1: int) -> List[str]:
    from itertools import permutations

    result = []
    if len(H0) < H1 or H1 < 1:
        return result
    result += (list(permutations(H0, H1)))

    return [''.join(i) for i in result]


#(54) A python function takes {H0,s:list,t:char} and {H1,t:int} as inputs. The function should return the list of all possible strings of length {H1,t:int} constructed from the characters in {H0,s:list,t:char}. Repeat characters are allowed.
def permutations_with_repeat_length_x(H0: List[str], H1: int) -> List[str]:
    from itertools import product

    result = []
    if len(H0) < H1 or H1 < 1:
        return result
    result += (list(product(H0, repeat=H1)))

    return [''.join(i) for i in result]


#(55) A python function takes {H0,s:list,t:char} and {H1,t:int} as inputs. The function should return the list of all possible strings of any length constructed from the characters in {H0,s:list,t:char}. Repeat characters are not allowed.
def all_permutations_no_repeat(H0: List[str]) -> List[str]:
    from itertools import permutations

    result = []
    if len(H0) < 1:
        return result
    for i in range(1, len(H0) + 1):
        result += (list(permutations(H0, i)))

    return [''.join(i) for i in result]


#(56) A python function takes {H0,s:list,t:char} as input. The function should return the list of all possible strings of any length constructed from the characters in {H0,s:list,t:char}. Repeat characters are allowed.
def all_permutations_with_repeat(H0: List[str]) -> List[str]:
    from itertools import product

    result = []
    if len(H0) < 1:
        return result
    for i in range(1, len(H0) + 1):
        result += (list(product(H0, repeat=i)))

    return [''.join(i) for i in result]


#(57) A python function takes {H0,s:list,t:obj}, {H1,t:obj} and {H2,t:int} as inputs. The function should insert {H1,t:obj} before index {H2,t:int} and returns the new list.
def insert_before_index(H0: List[object], H1: object, H2: int) -> List[object]:
    if H2 < 0:
        return H0
    elif H2 >= len(H0):
        H0.append(H1)
        return H0
    else:
        return H0[:H2] + [H1] + H0[H2:]


#(58) A python function takes {H0,s:list,t:obj}, {H1,t:obj} and {H2,t:int} as inputs. The function should insert {H1,t:obj} after index {H2,t:int} and returns the new list.
def insert_after_index(H0: List[object], H1: object, H2: int) -> List[object]:
    if H2 < 0:
        return H0
    elif H2 >= len(H0):
        H0.append(H1)
        return H0
    else:
        return H0[:H2 + 1] + [H1] + H0[H2 + 1:]


#(59) A python function takes {H0,s:list,t:obj}, {H1,t:obj} and {H2,t:obj}. The function should insert {H2,t:obj} before {H1,t:obj} in {H0,s:list,t:obj} and returns the new list.
def insert_before_element(H0: List[object], H1: object, H2: object) -> List[object]:
    if not H0:
        return []
    elif H1 not in H0:
        return H0
    else:
        n = H0.index(H1)
        return H0[:n] + [H2] + H0[n:]


#(60) A python function takes {H0,s:list,t:obj}, {H1,t:obj} and {H2,t:obj}. The function should insert {H2,t:obj} after {H1,t:obj} in {H0,s:list,t:obj} and returns the new list.
def insert_after_element(H0: List[object], H1: object, H2: object) -> List[object]:
    if not H0:
        return []
    elif H1 not in H0:
        return H0
    else:
        n = H0.index(H1)
        return H0[:n + 1] + [H2] + H0[n + 1:]


#(61) A python function takes a {H0,t:str} as input. The function should return characters with the lowest and highest ASCII values in {H0,t:str}.
def return_high_low_ascii(H0: str) -> tuple[str, str]:
    if H0 == '':
        return None
    d = {c: ord(c) for c in H0}

    return min(d), max(d)


#(62) A python function takes {H0,t:int,r:>0} as input. The function should return the binary representation of {H0,t:int,r:>0}.
def pos_int_to_binary(H0: int) -> str:
    result = ''
    while H0 >= 2:
        r = H0 % 2
        H0 = H0 // 2
        result += str(r)

    result += str(H0)

    return result[::-1]


#(63) A python function takes {H0,t:int} as input. The function should return true if {H0,t:int} is among the Fibonacci numbers otherwise it should return false.
def is_fibo(H0: int) -> bool:
    if H0 < 0:
        return False
    if H0 == 0 or H0 == 1:
        return True
    f0 = 0
    f1 = 1
    while True:
        f3 = f0 + f1
        if f3 == H0:
            return True
        elif f3 > H0:
            return False
        f0, f1 = f1, f3


#(64) A python function takes {H0,t:int} as input. The function should return the sum of first {H0,t:int} numbers of the Fibonacci sequence.
# For example, if n = 5, the function should return 0+1+1+2+3=7.
def sum_n_fibo(H0: int) -> int:
    s = 0
    if H0 <= 1:
        return s
    f0 = 0
    f1 = 1
    s += f1
    while H0 > 2:
        f3 = f0 + f1
        s += f3
        f0, f1 = f1, f3
        H0 -= 1

    return s


#(65) A python function takes {H0,t:int} as input. The function should return the list of all prime numbers among the first {H0,t:int} numbers of the Fibonacci sequence.
def prime_nums_fibo(H0: int) -> List[int]:
    result = []
    if H0 <= 3:
        return result
    fibo = [0, 1]
    f0 = 0
    f1 = 1
    while H0 > 2:
        f3 = f0 + f1
        fibo.append(f3)
        f0, f1 = f1, f3
        H0 -= 1

    flag = False
    for i in fibo[3:]:
        for j in range(2, i):
            if i % j == 0:
                flag = True
                break
        if flag:
            flag = False
        else:
            result.append(i)

    return result


#(66) A python function takes {H0,t:int} as input. The function should return the list of all composite numbers among the first {H0,t:int} numbers of the Fibonacci sequence.
def composite_nums_fibo(H0: int) -> List[int]:
    result = []
    if H0 < 7:
        return result
    fibo = [0, 1]
    f0 = 0
    f1 = 1
    while H0 > 2:
        f3 = f0 + f1
        fibo.append(f3)
        f0, f1 = f1, f3
        H0 -= 1

    for i in fibo[6:]:
        for j in range(2, i):
            if i % j == 0:
                result.append(i)
                break

    return result


#(67) A python function takes {H0,s:list,t:str} as input. The function should return a list of separate lists each containing strings from {H0,s:list,t:str} that are the same length.
def same_len_strings(H0: List[str]) -> list[list[str]]:
    if not H0:
        return []
    result = {}
    for i in H0:
        length = len(i)
        if length not in result:
            result[length] = [i]
        else:
            result[length].append(i)

    return list(result.values())


#(68) A python function takes {H0,t:str,c:sentence} as input. It should return a list of separate lists each containing strings without spaces from {H0,t:str,c:sentence} that are the same length.
def same_len_words(H0: str) -> list[list[str]]:
    if not H0:
        return []
    result = {}
    ls = H0.split()
    for i in ls:
        length = len(i)
        if length not in result:
            result[length] = [i]
        else:
            result[length].append(i)

    return list(result.values())


#(69) A python function takes {H0,t:str} and {H1,t:str} as inputs. The function should return true if {H0,t:str} and {H1,t:str} are anagrams otherwise it should return false.
def if_anagrams(H0: str, H1: str) -> bool:
    H0 = H0.replace(' ', '').lower()
    H1 = H1.replace(' ', '').lower()
    if len(H0) != len(H1):
        return False
    H0 = ''.join(sorted(H0))
    H1 = ''.join(sorted(H1))

    return H0 == H1


#(70) A python function takes {H0,s:list,t:str} as input. The function should return a list of distinct lists containing anagrams from {H0,s:list,t:str}.
# For example if the input is ['here', 'EvE', 'vee'] then the output should be [['here'], ['eve', 'vee']]
def all_anagrams(H0: List[str]) -> list[list[str]]:
    H0 = [i.replace(' ', '').lower() for i in H0]
    result = {}
    for i in H0:
        sorted_i = str(sorted(i))
        if sorted_i not in result:
            result[sorted_i] = [i]
        else:
            result[sorted_i].append(i)

    return list(result.values())


#(71) A python function takes {H0,s:list,t:str} as input. The function should return the list of all strings from {H0,s:list,t:str} that are real numbers.
# For example, if ['1.5', '2', '35t', 'one'] is given to the function, it should return ['1.5', '2'].
def find_numeric(H0: List[str]) -> List[str]:
    if not H0:
        return []
    try:
        float(H0[0])
        return [H0[0]] + find_numeric(H0[1:])
    except ValueError:
        return find_numeric(H0[1:])


#(72) A python function takes {H0,s:list,t:str} as input. The function should return the list of all alphanumeric strings from {H0,s:list,t:str}.
def find_alphanumeric(H0: List[str]) -> List[str]:
    if not H0:
        return []
    if H0[0].isalnum():
        return [H0[0]] + find_alphanumeric(H0[1:])
    else:
        return find_alphanumeric(H0[1:])


#(73) A python function takes {H0,t:int} as input. The function should return the string representation of {H0,t:int} with commas serving as the hundred separators.
def commas_hunds(H0: int) -> str:
    if -100 < H0 < 100:
        return H0
    flag = False
    if H0 < 0:
        flag = True
        H0 = -H0
    s = str(H0)[::-1]
    result = ''
    for i in range(0, len(s), 2):
        if i + 2 >= len(s):
            result += s[i:i + 2]
        else:
            result += s[i:i + 2] + ','

    if flag:
        return '-' + result[::-1]
    return result[::-1]


#(74) A python function takes {H0,t:int,r:>0} as input. The function should return true if {H0,t:int,r:>0} is a left-truncatable prime otherwise the function should return false.
def is_left_truncatable_prime(H0: int) -> bool:
    if '0' in str(H0) or H0 < 2:
        return False

    while H0 >= 2:
        length = len(str(H0))
        for i in range(2, H0):
            if H0 % i == 0:
                return False
        H0 = H0 % (10 ** (length - 1))

    if H0 == 1:
        return False

    return True


#(75) A python function takes {H0,t:int,r:>0} as input. The function should return true if the integer is a right-truncatable prime otherwise the function should return false.
def is_right_truncatable_prime(H0: int) -> bool:
    if '0' in str(H0) or H0 < 2:
        return False

    while H0 >= 2:
        for i in range(2, H0):
            if H0 % i == 0:
                return False
        H0 = H0 // 10

    if H0 == 1:
        return False

    return True


#(76) A python function takes {H0,t:int,r:>0} as input. The function should return true if {H0,t:int,r:>0} is a left-and-right-truncatable prime otherwise the function should return false.
def is_left_right_truncatable_prime(H0: int) -> bool:
    if '0' in str(H0) or H0 < 2:
        return False

    while H0 >= 2:
        length = len(str(H0))
        for i in range(2, H0):
            if H0 % i == 0:
                return False
        H0 = H0 % (10 ** (length - 1))
        H0 = H0 // 10

    if H0 == 1:
        return False

    return True


#(77) A python function takes {H0,t:str,c:sentence} as input. The function should return the list of all the words in {H0,t:str,c:sentence} that have duplicate characters.
# For example if the input is "Imperial College is a decent university" then the output should be ['College', 'decent', 'university'].
def words_with_duplicate_chars(H0: str) -> List[str]:
    result = []
    if len(H0) < 2:
        return result

    words = [i for i in H0.split()]
    for word in words:
        if len(set(word)) != len(word):
            result.append(word)

    return result


#(78) A python function takes {H0,t:str} as input. The function should return the list of all longest substrings of {H0,t:str} with no duplicate letters.
def longest_no_duplicate(H0: str) -> List[str]:
    from itertools import combinations

    if len(H0) == 1 or len(set(H0)) == len(H0):
        return H0

    all_no_dup = []
    length = len(H0) - 1
    while length > 0:
        chunks = [H0[i:j] for i, j in combinations(range(len(H0) + 1), r=2) if len(H0[i:j]) == length]
        for chunk in chunks:
            if len(set(chunk)) == len(chunk):
                all_no_dup.append(chunk)
        length -= 1

    dict = {}
    for i in all_no_dup:
        length = len(i)
        if length not in dict:
            dict[length] = [i]
        else:
            dict[length].append(i)
    print(dict)
    return list(set(dict[max(dict.keys())]))


#(79) A python function takes {H0,t:str} and {H1,t:int} as input. The function should return the list of all substrings of the length {H1,t:int} that do not contain any duplicate characters.
# For examle if the inputs are "Imperial" and 3 then the output should be ['Imp', 'mpe', 'per', 'eri', 'ria', 'ial'].
def length_x_no_duplicate(H0: str, H1: int) -> List[str]:
    from itertools import combinations

    if H1 > len(H0) or H1 <= 0:
        return []

    all_no_dup = []
    length = len(H0) - 1
    while length > 0:
        chunks = [H0[i:j] for i, j in combinations(range(len(H0) + 1), r=2) if len(H0[i:j]) == length]
        for chunk in chunks:
            if len(set(chunk)) == len(chunk):
                all_no_dup.append(chunk)
        length -= 1

    dict = {}
    for i in all_no_dup:
        length = len(i)
        if length not in dict:
            dict[length] = [i]
        else:
            dict[length].append(i)

    result = []
    for k, v in dict.items():
        if k == H1:
            result = v

    return result


#(80) A python function takes {H0,t:int,r:>0} as input. The function should return the least common multiple of all numbers ranging from 1 to {H0,t:int,r:>0} inclusive.
def divisible_by_nums_to_n(H0: int) -> int:
    from math import gcd

    if H0 < 1:
        return None
    result = 1
    for i in range(1, H0 + 1):
        result *= i // gcd(result, i)

    return result


#(81) A python function takes {H0,t:int,r:>0} and {H1,t:int,r:>0} as inputs. The function should return the least common multiple of all numbers between {H0,t:int,r:>0} and {H1,t:int,r:>0} inclusive.
def divisible_by_nums_x_y(H0: int, H1: int) -> int:
    from math import gcd

    if H0 < 1 or H1 < 1 or H1 < H0:
        return None

    if H0 == H1:
        return H0

    result = 1
    for i in range(H0, H1 + 1):
        result = result * i // gcd(result, i)

    return result


#(82) A python function takes a circular integer list {H0,s:list,t:int} as input. The function should return a contiguous sublist with the largest sum. If there is more than one such sublist, the function should return the list of all of them.
# For example if the input is [2, -7, -3, 1] then the function should return [1, 2].
def largest_sum_subarray(H0):
    dictionary = {sum(H0): [H0]}
    for j in range(len(H0)):
        temp_ls = H0[j:] + H0[:j]
        for i in range(1, len(temp_ls)):
            s = sum(temp_ls[:i])
            if s not in dictionary:
                dictionary[s] = [temp_ls[:i]]
            else:
                dictionary[s].append(temp_ls[:i])

    result = dictionary.get(max(dictionary.keys()))
    if len(result) == 1:
        return result[0]

    return result


#(83) A python function takes a circular integer list {H0,s:list,t:int} as input. It should return a contiguous sublist with the smallest sum in it. If there is more than one such sublist, the function should return the list of all of them.
# For example, if the input is [-2, 7, -3, 1] then the function should return [-3, 1, -2].
def smallest_sum_subarray(H0):
    dictionary = {sum(H0): [H0]}
    for j in range(len(H0)):
        temp_ls = H0[j:] + H0[:j]
        for i in range(1, len(temp_ls)):
            s = sum(temp_ls[:i])
            if s not in dictionary:
                dictionary[s] = [temp_ls[:i]]
            else:
                dictionary[s].append(temp_ls[:i])

    result = dictionary.get(min(dictionary.keys()))
    if len(result) == 1:
        return result[0]

    return result


#(84) A python function takes {H0,t:int} and a circular integer list {H1,s:list,t:int} as inputs. The function should return a contiguous sublist with a sum equal to {H0,t:int}. If there is more than one such sublist, the function should return the list of all of them.
# For example, if the inputs are [0, 7, -3, 1] and 1 then the function should return [[1], [1, 0]].
def sum_subarray_equal_n(H1, H0):
    dictionary = {sum(H1): [H1]}
    for j in range(len(H1)):
        temp_ls = H1[j:] + H1[:j]
        for i in range(1, len(temp_ls)):
            s = sum(temp_ls[:i])
            if s not in dictionary:
                dictionary[s] = [temp_ls[:i]]
            else:
                dictionary[s].append(temp_ls[:i])

    if H0 not in dictionary.keys():
        return []
    result = dictionary.get(H0)
    if len(result) == 1:
        return result[0]

    return result
    
    
#(85) A python function takes {H0,t:int,r:>0} as input. It should return the list of all combinations of positive integers in increasing order that add up to {H0,t:int,r:>0}.
def pre_combinations_add_up(n, *, boundary=1):
    for i in range(boundary, n - boundary + 1):
        for j in pre_combinations_add_up(n - i, boundary=i):
            yield (i,) + j
    if n >= boundary:
        yield n,


def combinations_add_up(H0):
    tuples = pre_combinations_add_up(H0)
    return [list(i) for i in tuples]


#(86) A python function takes {H0,s:list,t:int} as input. It should return the contiguous sublist of {H0,s:list,t:int} that has the highest element product. If there is more than one such sublist, the function should return the list of all of them.
# For example, if the input is [4, -3, 6, 1] then the function should return [[6], [6, 1]].
def max_product_subarray(H0):
    import math

    if len(H0) < 2:
        return H0
    
    dictionary = {}
    while len(H0) > 0:
        for i in range(1, len(H0) + 1):
            pr = math.prod(H0[:i])
            if pr not in dictionary:
                dictionary[pr] = [H0[:i]]
            else:
                dictionary[pr].append(H0[:i])
        H0.remove(H0[0])

    result = dictionary.get(max(dictionary.keys()))
    if len(result) == 1:
        return result[0]

    return result


#(87) A python function takes {H0,s:list,t:int} as input. The function should return the contiguous sublist with the minimum element product. If there is more than one such sublist, the function should return the list of all of them.
def min_product_subarray(H0):
    import math

    if len(H0) < 2:
        return H0
    
    dictionary = {}
    while len(H0) > 0:
        for i in range(1, len(H0) + 1):
            pr = math.prod(H0[:i])
            if pr not in dictionary:
                dictionary[pr] = [H0[:i]]
            else:
                dictionary[pr].append(H0[:i])

        H0.remove(H0[0])

    result = dictionary.get(min(dictionary.keys()))
    if len(result) == 1:
        return result[0]

    return result


#(88) A python function takes {H0,t:int} and a circular integer list {H1,s:list,t:int} as input. It should return a contiguous sublist with a product equal to {H0,t:int}. If there is more than one such sublist, the function should return the list of all of them.
def product_subarray_equal_n(H1, H0):
    import math

    if len(H1) < 2:
        return H1
    
    dictionary = {}
    while len(H1) > 0:
        for i in range(1, len(H1) + 1):
            pr = math.prod(H1[:i])
            if pr not in dictionary:
                dictionary[pr] = [H1[:i]]
            else:
                dictionary[pr].append(H1[:i])
        H1.remove(H1[0])

    if H0 not in dictionary.keys():
        return []
    result = dictionary.get(H0)
    if len(result) == 1:
        return result[0]

    return result


#(89) A Python function takes an integer list with distinct elements {H0,s:list,t:int,r:distinct} as input. The function should find the surpasser count for each list element, that is, the number of elements to the right that are greater than that element.
# For example, if the input is [6, 3, 5, 7], the function should return [1, 2, 1, 0]
def surpasser_count(H0):
    result = []
    if len(H0) <= 1 or len(H0) != len(set(H0)):
        return result
    c = 0
    for i in range(0, len(H0) - 1):
        for j in range(i + 1, len(H0)):
            if H0[j] > H0[i]:
                c += 1
        result.append(c)
        c = 0

    result.append(0)
    return result


#(90) A python function takes {H0,s:list,t:int}. THe function should return the list of all inversions of {H0,s:list,t:int}.
def find_inversions(H0):
    result = []
    if len(H0) <= 1:
        return result
    for i in range(0, len(H0)):
        for j in range(i + 1, len(H0)):
            if H0[j] < H0[i]:
                result.append([H0[i], H0[j]])

    return result


#(91) A python function takes a binary array {H0,s:list,t:int,c:binary} as input. The function should return the index of the first occurrence of 0 to be replaced with 1 to get the maximum length sequence of continuous 1's.
def first_zero_index(H0):
    # https://www.techiedelight.com/find-index-0-replaced-get-maximum-length-sequence-of-continuous-ones/
    if not H0 or H0.count(0) == 0:
        return None
    if len(H0) == 1:
        return H0[0]
    max_count = 0
    max_index = -1
    prev_zero_index = -1
    count = 0
    for i in range(len(H0)):
        if H0[i] == 1:
            count = count + 1
        else:
            count = i - prev_zero_index
            prev_zero_index = i

        if count > max_count:
            max_count = count
            max_index = prev_zero_index

    return max_index


#(92) A python function takes a matrix {H0,s:matrix,t:obj} as input. The function should return an element with the maximum number of occurrences in {H0,s:matrix,t:obj}. If more than one such element exists, then the function should return all of them.
def element_with_max_occurrences(H0):
    import itertools
    from collections import Counter

    occurrence = Counter(itertools.chain.from_iterable(H0))
    return [k for k, v in occurrence.items() if v == max(occurrence.values())]


#(93) A python function takes {H0,s:list,t:int} and {H1,s:list,t:int,r:sizeH0} the same size as inputs. The function should return the longest sublists from both lists that start and end at the same index in both lists and have the same sum.
# For example, if the inputs are [7, 13, 1, 6] and [0, 2, 12, 0] then the function should return ([13, 1], [2, 12]).
def longest_sublists_same_sum(H0, H1):
    if not H0 or not H1 or len(H0) != len(H1):
        return None
    d = []
    flag = False
    i_j_diff = 0
    for i in range(len(H0)):
        for j in range(i + 1, len(H0) + 1):
            if sum(H0[i:j]) == sum(H1[i:j]):
                if i_j_diff == j - i:
                    flag = True
                i_j_diff = j - i
                d.append((i, j))
    if not d:
        return None
    maxim = -1
    result = (-1, -1)

    if flag:
        sublists = []
        for tup in d:
            ii = tup[0]
            jj = tup[1]
            sublists.append((H0[ii:jj], H1[ii:jj]))
        return sublists

    for tup in d:
        diff = tup[1] - tup[0]
        if diff >= maxim:
            maxim = diff
            result = tup

    i = result[0]
    j = result[1]
    return H0[i:j], H1[i:j]


#(94) A python function takes {H0,s:list,t:int} and {H1,s:list,t:int,r:sizeH0} the same size as inputs. The function should return the longest sublists from both lists that start and end at the same index in both lists and have the same product.
# For example, if [2, 5, 1, 6] and [0, 1, 30, 1] are passed to the function then it should return ([5, 1, 6], [1, 30, 1]).
def longest_subarrays_same_product(H0, H1):
    from math import prod

    if not H0 or not H1 or len(H0) != len(H1):
        return None
    d = []
    for i in range(len(H0)):
        for j in range(i + 1, len(H0) + 1):
            if prod(H0[i:j]) == prod(H1[i:j]):
                d.append((i, j))

    if not d:
        return None
    maxim = -1
    result = (-1, -1)
    for tup in d:
        diff = tup[1] - tup[0]
        if diff > maxim:
            maxim = diff
            result = tup
    i = result[0]
    j = result[1]
    return H0[i:j], H1[i:j]


#(95) A python function takes {H0,t:int,r:>1} and {H1,s:list,t:int,r:>0} as inputs. The function should return all distinc lists of which elements are from {H1,s:list,t:int,r:>0} and each of which sum equals {H0,t:int,r:>1}. Repeat elements in the returned lists are allowed.
# For example, if the inputs are 4 and [1,2,3], then the function should return [[1,1,1,1],[1,1,2],[2,2],[1,3]].
from collections import namedtuple
class AbsComparator(int):
    def __lt__(self, other):
        if abs(int(self)) < abs(int(other)):
            return True
        elif abs(other) < abs(self):
            return False
        else:
            return int(self) < int(other)


def abs_lt(x, y):
    return AbsComparator(x) < AbsComparator(y)


class RecursiveSums(
    namedtuple('BaseRecursiveSums',
               ['value', 'repeat', 'skip', 'tail', 'prev'])):

    def sum_and_rest(self):
        if self.tail is None:
            if self.skip:
                yield [self.value] * self.repeat, [(self.value, self.skip)]
            else:
                yield [self.value] * self.repeat, []
        else:
            for partial_sum, rest in self.tail.sum_and_rest():
                for _ in range(self.repeat):
                    partial_sum.append(self.value)
                if self.skip:
                    rest.append((self.value, self.skip))
                yield partial_sum, rest
        if self.prev is not None:
            yield from self.prev.sum_and_rest()


def lexically_maximal_subset_rest(elements, target, bound=None):
    """
        elements = [(value, count), (value, count), ...]
            with largest absolute values first.
        target = target sum
        bound = a lexical bound on the maximal subset.
    """
    # First let's deal with all of the trivial cases.
    if 0 == len(elements):
        if 0 == target:
            yield []
    elif bound is None or 0 == len(bound):
        # Set the bound to something that trivially works.
        yield from lexically_maximal_subset_rest(elements, target, [abs(elements[0][0]) + 1])
    elif bound[0] < elements[0][0]:
        pass  # we automatically use more than the bound.
    else:
        # The trivial checks are done.

        bound_satisfied = (bound[0] != elements[0][0])

        # recurse_by_sum will have a key of (partial_sum, bound_index).
        # If the bound_index is None, the bound is satisfied.
        # Otherwise it will be the last used index in the bound.
        recurse_by_sum = {}
        # Populate it with all of the ways to use the first element at least once.
        (init_value, init_count) = elements[0]
        for i in range(init_count):
            if not bound_satisfied:
                if len(bound) <= i or bound[i] < init_value:
                    # Bound exceeded.
                    break
                elif init_value < bound[i]:
                    bound_satisfied = True
            if bound_satisfied:
                key = (init_value * (i + 1), None)
            else:
                key = (init_value * (i + 1), i)

            recurse_by_sum[key] = RecursiveSums(
                init_value, i + 1, init_count - i - 1, None, recurse_by_sum.get(key))

        # And now we do the dynamic programming thing.
        for j in range(1, len(elements)):
            value, repeat = elements[j]
            next_recurse_by_sum = {}
            for key, tail in recurse_by_sum.items():
                partial_sum, bound_index = key
                # Record not using this value at all.
                next_recurse_by_sum[key] = RecursiveSums(
                    value, 0, repeat, tail, next_recurse_by_sum.get(key))
                # Now record the rest.
                for i in range(1, repeat + 1):
                    if target < partial_sum + value * i:
                        break  # these are too big.

                    if bound_index is not None:
                        # Bounds check.
                        if len(bound) <= bound_index + i:
                            break  # bound exceeded.
                        elif bound[bound_index + i] < value:
                            break  # bound exceeded.
                        elif value < bound[bound_index + i]:
                            bound_index = None  # bound satisfied!
                    if bound_index is None:
                        next_key = (partial_sum + value * i, None)
                    else:
                        next_key = (partial_sum + value * i, bound_index + i)

                    next_recurse_by_sum[next_key] = RecursiveSums(
                        value, i, repeat - i, tail, next_recurse_by_sum.get(next_key))
            recurse_by_sum = next_recurse_by_sum

        # We now have all of the answers in recurse_by_sum, but in several keys.
        # Find all that may have answers.
        bound_index = len(bound)
        while 0 < bound_index:
            bound_index -= 1
            if (target, bound_index) in recurse_by_sum:
                yield from recurse_by_sum[(target, bound_index)].sum_and_rest()
        if (target, None) in recurse_by_sum:
            yield from recurse_by_sum[(target, None)].sum_and_rest()


def elements_split(elements, target, k, bound=None):
    if 0 == len(elements):
        if k == 0:
            yield []
    elif k == 0:
        pass  # still have elements left over.
    else:
        for (subset, rest) in lexically_maximal_subset_rest(elements, target, bound):
            for answer in elements_split(rest, target, k - 1, subset):
                answer.append(subset)
                yield answer


def list_of_equal_sum_split(H1, H0):
    if H0 < 1 or not H1:
        return None
    for i in H1:
        if i < 1:
            return None
    total = sum(H1)
    if (total % H0) != 0:
        return None
    else:
        target = total // H0
        counts = {}
        for e in sorted(H1, key=AbsComparator, reverse=True):
            counts[e] = 1 + counts.get(e, 0)
        elements = list(counts.items())
        result = elements_split(elements, target, H0)
        return [i for i in result]


#(96) A python function takes a circular integer list {H0,s:list,t:int} as input. The function should return a new list containing the next greater element for each element in {H0,s:list,t:int}. If there is no next greater element for an element, then the function should insert None in the corresponding index of the returned list. The next greater element of an element "x" in a list is the first larger number to the right side of "x".
def next_greater_element(H0):
    result = []
    if not H0:
        return result
    if len(H0) == 1:
        return [None]

    for i in range(len(H0)):
        temp_ls = H0[i:] + H0[:i]
        first_element = temp_ls[0]
        for j in range(1, len(temp_ls)):
            next_element = temp_ls[j]
            if next_element > first_element:
                result.append(next_element)
                break
            if j == len(temp_ls) - 1:
                result.append(None)

    return result


#(97) A python function takes {H0,s:matrix,t:float} and number {H1,t:int,r:>0} as inputs. The function should return a submatrix of size {H1,t:int,r:>0} by {H1,t:int,r:>0} in {H0,s:matrix,t:float} that has the largest sum.
def submatrix_size_n_with_max_sum(H0, H1):
    import math
    import numpy as np

    if not H0 or H1 < 1:
        return None
    if type(H0).__module__ != np.__name__:
        H0 = np.asmatrix(H0)
    max_sum = -math.inf
    submat = H0[:0, :0]
    height, width = H0.shape[0], H0.shape[1]
    for i in range(height - (H1 - 1)):
        for j in range(width - (H1 - 1)):
            square = H0[i:i + H1, j:j + H1]
            submat_sum = np.sum(square, dtype=np.float32)
            if submat_sum > max_sum:
                max_sum = submat_sum
                submat = square

    return submat


#(98) A python function takes {H0,s:matrix,t:float} as input. The function should return a square submatrix of in the given matrix that has the largest sum.
def square_submatrix_with_max_sum(H0):
    import math
    import numpy as np

    if not H0:
        return None
    if type(H0).__module__ != np.__name__:
        H0 = np.asmatrix(H0)
    max_sum = -math.inf
    submat = H0[:0, :0]
    height, width = H0.shape[0], H0.shape[1]

    boundary = max(height, width)
    for k in range(1, boundary + 1):
        for i in range(height - (k - 1)):
            for j in range(width - (k - 1)):
                square = H0[i:i + k, j:j + k]
                submat_sum = np.sum(square, dtype=np.float32)
                if submat_sum > max_sum:
                    max_sum = submat_sum
                    submat = square

    return submat


#(99) A python function takes {H0,s:matrix,t:float} as input. The function should return a submatrix of {H0,s:matrix,t:float} which has the largest sum.
def submatrix_with_max_sum(H0):
    import math
    import numpy as np

    if not H0:
        return None
    if type(H0).__module__ != np.__name__:
        H0 = np.asmatrix(H0)
    max_sum = -math.inf
    submatrix = H0[:0, :0]
    rows, columns = H0.shape[0], H0.shape[1]
    for c in range(rows):
        for i in range(columns):
            for j in range(1, columns + 1 - i):
                temp_submatrix = (H0[c:c + 1, i:i + j])
                submatrix_sum = np.sum(temp_submatrix, dtype=np.float32)
                if submatrix_sum > max_sum:
                    max_sum = submatrix_sum
                    submatrix = temp_submatrix

    for c in range(columns):
        for i in range(rows):
            for j in range(2, rows + 1 - i):
                temp_submatrix = (H0[i:i + j, c:c + 1])
                submatrix_sum = np.sum(temp_submatrix, dtype=np.float32)
                if submatrix_sum > max_sum:
                    max_sum = submatrix_sum
                    submatrix = temp_submatrix

    boundary = min(rows, columns)
    for k in range(2, boundary + 1):
        for c in range(rows - (k - 1)):
            for i in range((columns // k) + 1):
                for j in range(i + k, columns + 1):
                    temp_submatrix = (H0[c:c + k, i:j])
                    submatrix_sum = np.sum(temp_submatrix, dtype=np.float32)
                    if submatrix_sum > max_sum:
                        max_sum = submatrix_sum
                        submatrix = temp_submatrix

    return submatrix


#(100) A python function takes {H0,s:matrix,t:obj}. The function should return the count of all submatrices in {H0,s:matrix,t:obj}.
def count_all_submatrices(H0):
    import numpy as np

    if not H0:
        return None
    if type(H0).__module__ != np.__name__:
        H0 = np.asmatrix(H0)

    rows, columns = H0.shape[0], H0.shape[1]
    submatrix_count = 0

    for c in range(rows):
        for i in range(columns):
            for j in range(1, columns + 1 - i):
                submatrix_count += 1

    for c in range(columns):
        for i in range(rows):
            for j in range(2, rows + 1 - i):
                submatrix_count += 1

    boundary = min(rows, columns)
    for k in range(2, boundary + 1):
        for c in range(rows - (k - 1)):
            for i in range((columns // k) + 1):
                for j in range(i + k, columns + 1):
                    submatrix_count += 1

    return submatrix_count


#(101) A python function takes {H0,s:matrix,t:obj} and {H1,t:int,r:>0}. Among all submatrices in {H0,s:matrix,t:obj}, the function should return the count of submatrices that each has {H1,t:int,r:>0} elements.
def count_submatrices_of_size_n(H0, H1):
    import numpy as np

    if not H0 or H1 < 1:
        return None
    if type(H0).__module__ != np.__name__:
        H0 = np.asmatrix(H0)

    rows, columns = H0.shape[0], H0.shape[1]
    submatrix_of_size_n = 0

    for c in range(rows):
        for i in range(columns):
            for j in range(1, columns + 1 - i):
                temp_submatrix = (H0[c:c + 1, i:i + j])
                ro, co = temp_submatrix.shape[0], temp_submatrix.shape[1]
                if ro * co == H1:
                    submatrix_of_size_n += 1

    for c in range(columns):
        for i in range(rows):
            for j in range(2, rows + 1 - i):
                temp_submatrix = (H0[i:i + j, c:c + 1])
                ro, co = temp_submatrix.shape[0], temp_submatrix.shape[1]
                if ro * co == H1:
                    submatrix_of_size_n += 1

    boundary = min(rows, columns)
    for k in range(2, boundary + 1):
        for c in range(rows - (k - 1)):
            for i in range((columns // k) + 1):
                for j in range(i + k, columns + 1):
                    temp_submatrix = (H0[c:c + k, i:j])
                    ro, co = temp_submatrix.shape[0], temp_submatrix.shape[1]
                    if ro * co == H1:
                        submatrix_of_size_n += 1

    return submatrix_of_size_n