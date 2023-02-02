# A python function that returns the list of all integers from x to y both inclusive.
def all_ints_inclusive(x, y):
    return [i for i in range(x, y + 1) if x <= y]


# A python function that returns the list of all integers from x to y both exclusive.
def all_ints_exclusive(x, y):
    return [i for i in range(x + 1, y) if x < y]


# A python function that returns the list of all positive integers from x to y both inclusive.
def all_pos_ints_inclusive(x, y):
    return [i for i in range(x, y + 1) if x <= y and i > 0]


# A python function that returns the list of all positive integers from x to y both exclusive.
def all_pos_ints_exclusive(x, y):
    return [i for i in range(x + 1, y) if x < y and i > 0]


# A python function that returns the list of all negative integers from x to y both inclusive.
def all_neg_ints_inclusive(x, y):
    return [i for i in range(x, y + 1) if x <= y and i < 0]


# A python function that returns the list of all negative integers from x to y both exclusive.
def all_neg_ints_exclusive(x, y):
    return [i for i in range(x + 1, y) if x < y and i < 0]


# A python function that returns the list of all even integers from x to y both inclusive.
def all_even_ints_inclusive(x, y):
    return [i for i in range(x, y + 1) if x <= y and i % 2 == 0]


# A python function that returns the list of all even integers from x to y both exclusive.
def all_even_ints_exclusive(x, y):
    return [i for i in range(x + 1, y) if x < y and i % 2 == 0]


# A python function that returns the list of all odd integers from x to y both inclusive.
def all_odd_ints_inclusive(x, y):
    return [i for i in range(x, y + 1) if x <= y and i % 2 != 0]


# A python function that returns the list of all odd integers from x to y both exclusive.
def all_odd_ints_exclusive(x, y):
    return [i for i in range(x + 1, y) if x < y and i % 2 != 0]


# A python function that returns the list of all integers from x to y that are divisible by n. Both x and y should be inclusive.
def all_ints_div_by_n_inclusive(x, y, n):
    return [i for i in range(x, y + 1) if x <= y and i % n == 0]


# A python function that returns the list of all integers from x to y that are divisible by n. Both x and y should be exclusive.
def all_ints_div_by_n_exclusive(x, y, n):
    return [i for i in range(x + 1, y) if x < y and i % n == 0]


# A python function that returns the list of all integers from x to y that are not divisible by n. Both x and y should be inclusive.
def all_ints_not_div_by_n_inclusive(x, y, n):
    return [i for i in range(x, y + 1) if x <= y and i % n != 0]


# A python function that returns the list of all integers from x to y that are divisible by m and n. Both x and y should be inclusive.
def all_ints_div_by_m_n_inclusive(x, y, m, n):
    return [i for i in range(x, y + 1) if x <= y and i % m == 0 and i % n == 0]


# A python function that returns the list of all integers from x to y that are divisible by m or by n. Both x and y should be inclusive.
def all_ints_div_by_m_n_inclusive(x, y, m, n):
    return [i for i in range(x, y + 1) if x <= y and i % m == 0 or i % n == 0]


# A python function that returns the sum of all integers from x to y inclusive.
def sum_ints(x, y):
    return sum(range(x, y + 1))


# A python function that returns the sum of all even integers from x to y inclusive.
def sum_even_ints(x, y):
    return sum([i for i in range(x, y + 1) if i % 2 == 0])


# A python function that returns the sum of all odd integers from x to y inclusive.
def sum_odd_ints(x, y):
    return sum([i for i in range(x, y + 1) if i % 2 != 0])


# A python function that returns the sum of all integers from x to y that are divisible by n. Both x and y are inclusive.
def sum_ints_div_by_n(x, y, n):
    return sum([i for i in range(x, y + 1) if i % n == 0])


# A python function that take an integer and returns the list of all positive divisors of that integer.
def all_divs(n):
    result = []
    if n <= 0:
        return result
    return [i for i in range(1, n + 1) if n % i == 0]


# A python function that take an integer and returns the sum of all positive divisors of that integer.
def sum_all_divs(n):
    result = []
    if n <= 0:
        return sum(result)
    return sum([i for i in range(1, n + 1) if n % i == 0])


# A python function that returns the list of all prime numbers up to n inclusive.
def prime_nums(n):
    result = []
    if n <= 1:
        return result
    else:
        flag = False
        for i in range(2, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    flag = True
                    break
            if flag:
                flag = False
            else:
                result.append(i)
        return result


# A python function that returns the sum of all prime numbers up to n inclusive.
def sum_prime_nums(n):
    result = []
    if n <= 1:
        return sum(result)
    else:
        flag = False
        for i in range(2, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    flag = True
                    break
            if flag:
                flag = False
            else:
                result.append(i)
        return sum(result)


# A python function that returns the list of all prime numbers between x and y both inclusive.
def prime_nums_x_y(x, y):
    result = []
    if x > y:
        return result
    elif x <= 1 and y <= 1:
        return result
    elif x <= 1:
        return prime_nums_x_y(2, y)
    else:
        flag = False
        for i in range(x, y + 1):
            for j in range(2, i):
                if i % j == 0:
                    flag = True
                    break
            if flag:
                flag = False
            else:
                result.append(i)
        return result


# A python function that returns the sum of all prime numbers between x and y both inclusive.
def sum_prime_nums_x_y(x, y):
    result = []
    if x > y:
        return sum(result)
    elif x <= 1 and y <= 1:
        return sum(result)
    elif x <= 1:
        return sum_prime_nums_x_y(2, y)
    else:
        flag = False
        for i in range(x, y + 1):
            for j in range(2, i):
                if i % j == 0:
                    flag = True
                    break
            if flag:
                flag = False
            else:
                result.append(i)
        return sum(result)


# A python function that takes an integer and returns a list of all composite numbers up to the integer inclusive.
def find_composite_numbers(n):
    result = []
    if n < 4:
        return result
    else:
        for i in range(4, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    result.append(i)
                    break
    return result


# A python function that takes two integers and returns a list of all composite numbers between the two integers inclusive.
def find_composite_nums_x_y(x, y):
    result = []
    if x > y:
        return result
    if x < 4:
        x = 4
    for i in range(x, y + 1):
        for j in range(2, i):
            if i % j == 0:
                result.append(i)
                break
    return result


# A python function that returns the greatest common factor of x and y.
def gcf(x, y):
    result = None
    if x == 0 and y == 0:
        return result
    elif x < 0:
        return gcf(-x, y)
    elif y < 0:
        return gcf(x, -y)
    elif x == 0:
        return y
    elif y == 0:
        return x
    else:
        x_factors = [i for i in range(1, x + 1) if x % i == 0]
        y_factors = [i for i in range(1, y + 1) if y % i == 0]
        for i in reversed(x_factors):
            if i in y_factors:
                result = i
                break
        return result


# A python function that returns the greatest common factor of x and y and z.
def gcf(x, y, z):
    result = None
    if x == 0 and y == 0 and z == 0:
        return result
    elif x < 0:
        return gcf(-x, y, z)
    elif y < 0:
        return gcf(x, -y, z)
    elif z < 0:
        return gcf(x, y, -z)
    else:
        if x == 0:
            x_factors = [i for i in range(0, max(y, z) + 1)]
        else:
            x_factors = [i for i in range(1, x + 1) if x % i == 0]
        if y == 0:
            y_factors = [i for i in range(0, max(x, z) + 1)]
        else:
            y_factors = [i for i in range(1, y + 1) if y % i == 0]
        if z == 0:
            z_factors = [i for i in range(0, max(x, y) + 1)]
        else:
            z_factors = [i for i in range(1, z + 1) if z % i == 0]

        for i in reversed(x_factors):
            if i in y_factors and i in z_factors:
                result = i
                break
        return result


# A python function that takes a positive integer and returns true if the integer is a perfect number otherwise it should return false.
def is_perfect_number(n):
    if n <= 0:
        return False
    return sum([i for i in range(1, n) if n % i == 0]) == n


# A python function that returns the list of all perfect numbers up to x inclusive.
def all_perfect_numbers(x):
    result = []
    if x <= 0:
        return result
    for n in range(1, x + 1):
        if sum([i for i in range(1, n) if n % i == 0]) == n:
            result.append(n)
    return result


####### List relayted questions #######

# A python function that takes a list and returns the largest element of the list.
def largest_element(l):
    if not l:
        return None

    return max(l)


# A python function that takes a list and returns the second largest element of the list.
# For example if the list is [0,1,2] the second largest element is 1.
# For example if the list is [0,1,2,2] the second largest element is 2.
def second_largest_element(l):
    if len(l) <= 1:
        return None
    l.sort()

    return l[-2]


# A python function that takes a list and returns the n-th largest element of the list.
# For example if the list is [2,2,2,2] the fourth largest element is 2.
# For example if the list is [7,7,0,1,0,1,5] the fourth largest element is 1.
def nth_largest_element(l, n):
    if len(l) < n or n <= 0:
        return None
    l.sort()

    return l[-n]


# A python function that takes a list and returns the smallest element of the list.
def smallest_element(l):
    if not l:
        return None

    return min(l)


# A python function that takes a list and returns the second smallest element of the list.
# For example if the list is [0,1,2] the second smallest element is 1.
# For example if the list is [2,0,1,0,1] the second smallest element is 0.
# For example if the list is [2,1,0,1,1,2] the second smallest element is 1.
def second_smallest_element(l):
    if len(l) <= 1:
        return None
    l.sort()

    return l[1]


# A python function that takes a list and returns the n-th smallest element of the list.
# For example if the list is [2,2,2,2] the fourth smallest element is 2.
# For example if the list is [7,7,0,1,0,1,5] the fourth smallest element is 1.
def nth_smallest_element(l, n):
    if len(l) < n or n <= 0:
        return None
    l.sort()

    return l[n - 1]


# A python function takes two lists and return a new list of all similar elements.
def similar_elements(l1, l2):
    result = []
    if not l1 or not l2:
        return result

    for i in l1:
        if i in l2 and i not in result:
            result.append(i)

    return result


# A python function that takes a list and returns the list of all sublists of the original list.
def all_sublists(l):
    from itertools import combinations

    result = []
    for i in range(0, len(l) + 1):
        result = result + (list(combinations(l, i)))

    return [list(i) for i in result]


# A python function that takes a list and returns the list of all sublists of length n of the original list.
def all_sublists_length_n(l, n):
    from itertools import combinations

    result = []
    if n > len(l) or n < 0:
        return result
    result = result + (list(combinations(l, n)))

    return [list(i) for i in result]


# A python function that takes two lists l1 and l2 and returns true if either is a sublist of the other otherwise, it should return false.
def if_sublist(l1, l2):
    if l1 == [] or l2 == []:
        return True

    result1 = False
    result2 = False
    c1 = 0
    c2 = 0

    if len(l1) < len(l2):
        for i in l1:
            if i in l2:
                c1 += 1
        if len(l1) == c1:
            result1 = True

    else:
        for i in l2:
            if i in l1:
                c2 += 1
        if len(l2) == c2:
            result1 = True

    return result1 or result2


# A Python function takes an array of n lists.
# The function should return a list where all the elements of the given array are sublists of the returned list.
def original_list(l):
    import itertools

    return list(itertools.chain.from_iterable(l))


# A python function that takes a list and removes duplicates from the list and returns the new list.
def remove_duplicate(l):
    result = []
    if not l:
        return result

    for i in l:
        if i not in result:
            result.append(i)

    return result


# A python functon that takes a list of numbers and returns the average of the numbers.
def mean_of_list(l):
    return sum(l) / len(l)


# A python functon that takes a list of numbers and returns the mode of the numbers.
# If the given list has more than one mode then the function should return all of them.
def mode_of_list(l):
    import operator

    result = []
    d = {num: l.count(num) for num in l}
    if all(v == 1 for v in d.values()):
        return result
    sorted_d = (dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True)))
    largest = list(sorted_d.values())[0]
    for k, v in sorted_d.items():
        if v == largest:
            result.append(k)

    return result


# A python function that takes a string and returns the list of all characters of the string.
def string_chars(s):
    result = []
    if s == '':
        return result

    return [c for c in s]


# A python function that takes a string and returns the number of all vowels (both lower case and upper case) in the string.
def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    s = s.lower()
    for c in s:
        if c in vowels:
            count += 1

    return count


# A python function that takes a string of length at least three and finds all palindrome sequences of size x in the string.
# The function should return the list of the palindrome sequences. If there is no palindrome sequence of size x in the string, the function should return None.
# For example, a palindrome sequence of size 3 in "ev en" is "eve".
# For example, a palindrome sequence of size 4 in "Yesterday we met Anna" is "anna".
def find_all_palindrome_x(s, x):
    if len(s) <= 2 or x <= 2 or x > len(s):
        return None

    s = s.lower()
    s = s.replace(" ", "")
    all_palindrome = []
    for i in range(0, len(s)):
        chunk = s[i:i + x]
        if len(chunk) < x:
            break
        if chunk == chunk[::-1]:
            all_palindrome.append(chunk)

    if len(all_palindrome) > 0:
        return all_palindrome
    else:
        return None


# A python function that takes a string of length at least three and finds all palindrome sequences of size at least three in the string.
# The function should return the list of the palindrome sequences. If there is no palindrome sequence in the string, the function should return None.
# For example, if "ev en" is given to the function, it should return ['eve'].
# For example, if "Imperial College" is given to the function, it should return ['ege'].
# For example, if "Yesterday we met Anna" is given to the function, it should return ['eme', 'anna'].
def find_all_palindrome(s):
    if len(s) <= 2:
        return None
    s = s.lower()
    s = s.replace(" ", "")
    c = 3
    all_palindrome = []
    for _ in range(0, len(s) - 2):
        for i in range(0, len(s)):
            chunk = s[i:i + c]
            if len(chunk) < c:
                break
            if chunk == chunk[::-1]:
                all_palindrome.append(chunk)
        c += 1

    if len(all_palindrome) > 0:
        return all_palindrome
    else:
        return None


# A python function that takes a list of characters and returns the list of all possible palindrome sequences of length x made out of only those characters.
# For example, if the function takes ['e','v','a','e'] it should return ['eve', 'eae'].
def all_palindrome_length_3(l, x):
    from itertools import combinations

    result = []
    if len(l) < x or x < 3 or len(l) < 3:
        return result
    result = result + (list(combinations(l, x)))

    return [''.join(i) for i in result if i == i[::-1]]


# A Python function that accepts a list of characters and produces a list of all palindrome sequences that can be created using only those characters. All returned palindrome sequences must be at least three characters long.
# For example, if the function takes ['t', 'e', 's', 'e', 't'] it should return ['tet', 'tst', 'tet', 'ese', 'teet', 'teset'].
def all_palindrome_all_length(l):
    from itertools import combinations

    result = []
    if len(l) < 3:
        return result
    for i in range(3, len(l) + 1):
        result = result + (list(combinations(l, i)))

    return [''.join(i) for i in result if i == i[::-1]]


# A python function that takes a list of characters and returns the list of
# all possible strings of length x constructed from those characters. Repeat characters are not allowed.
def permutations_no_repeat_length_x(l, x):
    from itertools import permutations

    result = []
    if len(l) < x or x < 1:
        return result
    result = result + (list(permutations(l, x)))

    return [''.join(i) for i in result]


# A python function that takes a list of characters and returns the list of
# all possible strings of length x constructed from those characters. Repeat characters are allowed.
def permutations_with_repeat_length_x(l, x):
    from itertools import product

    result = []
    if len(l) < x or x < 1:
        return result
    result = result + (list(product(l, repeat=x)))

    return [''.join(i) for i in result]


# A python function that takes a list of characters and returns the list of
# all possible strings of any length constructed from those characters. Repeat characters are not allowed.
def all_permutations_no_repeat(l):
    from itertools import permutations

    result = []
    if len(l) < 1:
        return result
    for i in range(1, len(l) + 1):
        result = result + (list(permutations(l, i)))

    return [''.join(i) for i in result]


# A python function that takes a list of characters and returns the list of
# all possible strings of any length constructed from those characters. Repeat characters are allowed.
def all_permutations_with_repeat(l):
    from itertools import product

    result = []
    if len(l) < 1:
        return result
    for i in range(1, len(l) + 1):
        result = result + (list(product(l, repeat=i)))

    return [''.join(i) for i in result]


# A python function that takes a list and inserts a given element before a given index and returns the new list.
def insert_before_index(l, e, n):
    if n < 0:
        return l
    elif n >= len(l):
        l.append(e)
        return l
    else:
        return l[:n] + [e] + l[n:]


# A python function that takes a list and inserts a given element after a given index and returns the new list.
def insert_after_index(l, e, n):
    if n < 0:
        return l
    elif n >= len(l):
        l.append(e)
        return l
    else:
        return l[:n + 1] + [e] + l[n + 1:]


# A python function that takes a list and inserts a given element before an element in the list and returns the new list.
def insert_before_element(l, list_e, given_e):
    if not l:
        return []
    elif list_e not in l:
        return l
    else:
        n = l.index(list_e)
        return l[:n] + [given_e] + l[n:]


# A python function that takes a list and inserts a given element after an element in the list and returns the new list.
def insert_after_element(l, list_e, given_e):
    if not l:
        return []
    elif list_e not in l:
        return l
    else:
        n = l.index(list_e)
        return l[:n + 1] + [given_e] + l[n + 1:]


# A python function that takes a string and returns characters with the lowest and highest ASCII values, respectively.
def return_high_low_ascii(s):
    if s == '':
        return None
    d = {c: ord(c) for c in s}

    return min(d), max(d)


# A python function that takes a positive integer and returns the binary representation of the given integer.
def pos_int_to_binary(n):
    result = ''
    while n >= 2:
        r = n % 2
        n = n // 2
        result += str(r)

    result += str(n)

    return result[::-1]


# A python function that takes an integer and returns true if the integer is among the Fibonacci numbers otherwise it should return false.
def is_fibo(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    f0 = 0
    f1 = 1
    while True:
        f3 = f0 + f1
        if f3 == n:
            return True
        elif f3 > n:
            return False
        f0, f1 = f1, f3


# A python function that returns the sum of first n numbers of the Fibonacci sequence.
# For example, if n = 5, the function should return 0+1+1+2+3=7.
def sum_n_fibo(n):
    s = 0
    if n <= 1:
        return s
    f0 = 0
    f1 = 1
    s += f1
    while n > 2:
        f3 = f0 + f1
        s += f3
        f0, f1 = f1, f3
        n -= 1

    return s


# A python function that returns the list of all prime numbers among the first n numbers of the Fibonacci sequence.
def prime_nums_fibo(n):
    result = []
    if n <= 3:
        return result
    fibo = [0, 1]
    f0 = 0
    f1 = 1
    while n > 2:
        f3 = f0 + f1
        fibo.append(f3)
        f0, f1 = f1, f3
        n -= 1

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


# A python function that returns the list of all composite numbers among the first n numbers of the Fibonacci sequence.
def composite_nums_fibo(n):
    result = []
    if n < 7:
        return result
    fibo = [0, 1]
    f0 = 0
    f1 = 1
    while n > 2:
        f3 = f0 + f1
        fibo.append(f3)
        f0, f1 = f1, f3
        n -= 1

    for i in fibo[6:]:
        for j in range(2, i):
            if i % j == 0:
                result.append(i)
                break

    return result


# A python function takes a list of strings as input. It should return a list of separate lists each containing
# strings from the given list that are the same length.
def same_len_strings(ls):
    result = {}
    for i in ls:
        length = len(i)
        if length not in result:
            result[length] = [i]
        else:
            result[length].append(i)

    return list(result.values())


# A python function that takes two strings and returns true if they are anagrams otherwise it should return false.
def if_anagrams(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if len(s1) != len(s2):
        return False
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))

    return s1 == s2


# A python function that takes a list of strings as input and returns a list of distinct lists containing
# anagrams from the given list.
def all_anagrams(ls):
    ls = [i.replace(' ', '').lower() for i in ls]
    result = {}
    for i in ls:
        sorted_i = str(sorted(i))
        if sorted_i not in result:
            result[sorted_i] = [i]
        else:
            result[sorted_i].append(i)

    return list(result.values())


# A python function takes an array of strings as input. It should return the list of all strings from the given array that are numbers of any type.
# For example, if ['1.5', '2', '35t', 'one'] is given to the function, it should return ['1.5', '2'].
def find_numeric(ls):
    if not ls:
        return []
    try:
        float(ls[0])
        return [ls[0]] + find_numeric(ls[1:])
    except ValueError:
        return find_numeric(ls[1:])


# A python function takes an array of strings as input. It should return the list of all alphanumeric strings from the given array.
def find_alphanumeric(ls):
    if not ls:
        return []
    if ls[0].isalnum():
        return [ls[0]] + find_alphanumeric(ls[1:])
    else:
        return find_alphanumeric(ls[1:])


# A python function takes an integer as input. It should return the string representation of the integer with commas serving as the hundred separators.
def commas_hunds(n):
    if -100 < n < 100:
        return n
    flag = False
    if n < 0:
        flag = True
        n = -n
    s = str(n)[::-1]
    result = ''
    for i in range(0, len(s), 2):
        if i + 2 >= len(s):
            result = result + s[i:i + 2]
        else:
            result = result + s[i:i + 2] + ','

    if flag:
        return '-' + result[::-1]
    return result[::-1]


# A python function that takes a positive integer and returns true if the integer is a left-truncatable prime otherwise the function should return false.
def is_left_truncatable_prime(n):
    if '0' in str(n) or n < 2:
        return False

    while n >= 2:
        length = len(str(n))
        for i in range(2, n):
            if n % i == 0:
                return False
        n = n % (10 ** (length - 1))

    if n == 1:
        return False

    return True


# A python function that takes a positive integer and returns true if the integer is a right-truncatable prime otherwise the function should return false.
def is_right_truncatable_prime(n):
    if '0' in str(n) or n < 2:
        return False

    while n >= 2:
        for i in range(2, n):
            if n % i == 0:
                return False
        n = n // 10

    if n == 1:
        return False

    return True


# A python function that takes a positive integer and returns true if the integer is a left-and-right-truncatable prime otherwise the function should return false.
def is_left_right_truncatable_prime(n):
    if '0' in str(n) or n < 2:
        return False

    while n >= 2:
        length = len(str(n))
        for i in range(2, n):
            if n % i == 0:
                return False
        n = n % (10 ** (length - 1))
        n = n // 10

    if n == 1:
        return False

    return True


# A python function takes a sentence as input. It should return the list of all the words in the sentence that have duplicate characters.
def words_with_duplicate_chars(s):
    result = []
    if len(s) < 2:
        return result

    words = [i for i in s.split()]
    for word in words:
        if len(set(word)) != len(word):
            result.append(word)

    return result


# A python function takes a string as input. It should return the list of all longest substrings of the input with no duplicate letters.
def longest_no_duplicate(s):
    from itertools import combinations

    if len(s) == 1 or len(set(s)) == len(s):
        return s

    all_no_dup = []
    length = len(s) - 1
    while length > 0:
        chunks = [s[i:j] for i, j in combinations(range(len(s) + 1), r=2) if len(s[i:j]) == length]
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


# A python function takes a string as input. It should return the list of all substrings of the length x that do not contain any duplicate characters.
def length_x_no_duplicate(s, x):
    from itertools import combinations

    if x > len(s) or x <= 0:
        return []

    all_no_dup = []
    length = len(s) - 1
    while length > 0:
        chunks = [s[i:j] for i, j in combinations(range(len(s) + 1), r=2) if len(s[i:j]) == length]
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
        if k == x:
            result = v

    return result


# A python function takes a positive integer as input. It should return the least common multiple of
# all numbers ranging from 1 to the given integer inclusive.
def divisible_by_nums_to_n(n):
    from math import gcd

    if n < 1:
        return None
    result = 1
    for i in range(1, n + 1):
        result = result * i // gcd(result, i)

    return result


# A python function takes two positive integer as inputs. It should return the least common multiple of
# all numbers between the given integers inclusive.
def divisible_by_nums_x_y(x, y):
    from math import gcd

    if x < 1 or y < 1 or y < x:
        return None

    if x == y:
        return x

    result = 1
    for i in range(x, y + 1):
        result = result * i // gcd(result, i)

    return result


# A python function takes a circular integer array as input. It should return a contiguous subarray with the largest sum in it. If there is more than one of such subarrays, the function should return the list of all of them.
def largest_sum_subarray(ls):
    dictionary = {}
    dictionary[sum(ls)] = [ls]
    for j in range(len(ls)):
        temp_ls = ls[j:] + ls[:j]
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


# A python function takes a circular integer array as input. It should return a contiguous subarray with the smallest sum in it. If there is more than one of such subarrays, the function should return the list of all of them.
def smallest_sum_subarray(ls):
    dictionary = {}
    dictionary[sum(ls)] = [ls]
    for j in range(len(ls)):
        temp_ls = ls[j:] + ls[:j]
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


# A python function takes a circular integer array as input. It should return a contiguous subarray with a sum equal to a given number. If there is more than one of such subarrays, the function should return the list of all of them.
def sum_subarray_equal_n(ls, n):
    dictionary = {}
    dictionary[sum(ls)] = [ls]
    for j in range(len(ls)):
        temp_ls = ls[j:] + ls[:j]
        for i in range(1, len(temp_ls)):
            s = sum(temp_ls[:i])
            if s not in dictionary:
                dictionary[s] = [temp_ls[:i]]
            else:
                dictionary[s].append(temp_ls[:i])

    if n not in dictionary.keys():
        return []
    result = dictionary.get(n)
    if len(result) == 1:
        return result[0]

    return result
    
    
# A python function takes a positive number as input. It should return the list of all combinations of positive integers in increasing order that add up to the given positive number.
def pre_combinations_add_up(n, *, boundary=1):
    for i in range(boundary, n - boundary + 1):
        for j in pre_combinations_add_up(n - i, boundary=i):
            yield (i,) + j
    if n >= boundary:
        yield n,


def combinations_add_up(n):
    tuples = pre_combinations_add_up(n)
    return [list(i) for i in tuples]


# A python function takes an array as input. It should return the contiguous sub-array with the highest element product.
# If there is more than one of such sub-arrays, the function should return the list of all of them.
def max_product_subarray(ls):
    import math
    
    if len(ls) < 2:
        return ls
    dictionary = {}
    dictionary[math.prod(ls)] = [ls]

    while len(ls) > 0:
        for i in range(1, len(ls) + 1):
            pr = math.prod(ls[:i])
            if pr not in dictionary:
                dictionary[pr] = [ls[:i]]
            else:
                dictionary[pr].append(ls[:i])

        ls.remove(ls[0])

    result = dictionary.get(max(dictionary.keys()))
    if len(result) == 1:
        return result[0]

    return result


# A python function takes an array as input. It should return the contiguous sub-array with the minimum element product.
# If there is more than one of such sub-arrays, the function should return the list of all of them.
def min_product_subarray(ls):
    import math

    if len(ls) < 2:
        return ls
    dictionary = {}
    dictionary[math.prod(ls)] = [ls]

    while len(ls) > 0:
        for i in range(1, len(ls) + 1):
            pr = math.prod(ls[:i])
            if pr not in dictionary:
                dictionary[pr] = [ls[:i]]
            else:
                dictionary[pr].append(ls[:i])

        ls.remove(ls[0])

    result = dictionary.get(min(dictionary.keys()))
    if len(result) == 1:
        return result[0]

    return result


# A python function takes a circular integer array as input. It should return a contiguous subarray with a product equal to a given number.
# If there is more than one of such subarrays, the function should return the list of all of them.
def product_subarray_equal_n(ls, n):
    import math

    if len(ls) < 2:
        return ls
    dictionary = {}
    dictionary[math.prod(ls)] = [ls]

    while len(ls) > 0:
        for i in range(1, len(ls) + 1):
            pr = math.prod(ls[:i])
            if pr not in dictionary:
                dictionary[pr] = [ls[:i]]
            else:
                dictionary[pr].append(ls[:i])

        ls.remove(ls[0])
    
    if n not in dictionary.keys():
        return []
    result = dictionary.get(n)
    if len(result) == 1:
        return result[0]

    return result
