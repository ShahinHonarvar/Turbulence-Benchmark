import random
import string


def input_generator(ls, c, size):
    data_structure = ls[1]
    type_ = ls[2]
    if data_structure == '':
        if type_ == 'int' and c == 0:
            return small_int_generator()
        if type_ == 'int' and c == 1:
            return medium_int_generator(ls[3])
        if type_ == 'int' and c > 1:
            return large_int_generator()
        elif type_ == 'float':
            return float_generator(ls[3])
        elif type_ == 'obj':
            return obj_generator()
        elif type_ == 'str':
            return str_generator(ls[3])
    elif data_structure == 'list':
        length = random.randint(0, 10)
        r = ls[3]
        if type_ == 'int' and r == 'distinct':
            ls_int = []
            counter = 0
            while counter < length:
                int_ = medium_int_generator('')
                if int_ not in ls_int:
                    ls_int.append(int_)
                    counter += 1
            return ls_int
        elif type_ == 'int' and size >= -1:
            if size == -1:
                return [random.randint(-10, 10) for _ in range(length)]
            return [random.randint(-10, 10) for _ in range(size)]
        elif type_ == 'int' and r == 'binary':
            return [random.randint(0, 1) for _ in range(length)]
        elif type_ == 'int':
            return [medium_int_generator(r) for _ in range(length)]
        elif type_ == 'float':
            return [float_generator(r) for _ in range(length)]
        elif type_ == 'obj':
            return [obj_generator() for _ in range(length)]
        elif type_ == 'char':
            return [letters_string_generator(1, False) for _ in range(length)]
        elif type_ == 'str':
            return [str_generator(r) for _ in range(length)]
    elif data_structure == 'matrix':
        return matrix_generator(type_)


def small_int_generator():
    return random.randint(-100, 10)


def medium_int_generator(r):
    if not r:
        return random.randint(11, 100)
    else:
        start = int(r[-1])
        return random.randint(start + 1, 100)


def large_int_generator():
    return random.randint(101, 1000)


def float_generator(r):
    if not r:
        return random.uniform(-100.0, 100.0)
    else:
        start = int(r[-1])
        return random.uniform(start + 0.1, 100.0)


def str_generator(r):
    if not r:
        length = random.randint(2, 20)
        a = palindrome_generator()
        b = alphanumeric_generator(length, True)
        c = punc_string_generator(length, True)
        ls = [a, b, c]
        random.shuffle(ls)
        return ls[0] + ls[1] + ls[2]
    elif r == 'palin':
        length = random.randint(2, 5)
        a = palindrome_generator()
        b = alphanumeric_generator(length, True)
        c = punc_string_generator(length, True)
        ls = [a, b, c]
        random.shuffle(ls)
        return ls[0] + ' ' + ls[1] + ' ' + ls[2]
    elif r == 'sentence':
        rounds = random.randint(2, 15)
        sentence = ''
        for i in range(rounds):
            sentence += English_word_generator()
            if i == rounds - 1:
                sentence += '.'
                break
            sentence += ' '
        return sentence
    elif r == 'anagram':
        return anagram_generator(English_word_generator())
    elif r == 'alnum':
        length = random.randint(2, 5)
        return alphanumeric_generator(length, True)
    elif r == 'alnum&num':
        option = random.randint(1, 4)
        if option == 1:
            return digit_string_generator(3, True)
        elif option == 2:
            return str(float_generator(''))
        elif option == 3:
            return alphanumeric_generator(5, False)
        else:
            return English_word_generator()


def letters_string_generator(length, rep):
    if rep:
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))
    else:
        return ''.join(random.sample(string.ascii_letters, length))


def digit_string_generator(length, rep):
    if rep:
        return ''.join(random.choice(string.digits) for _ in range(length))
    else:
        return ''.join(random.sample(string.digits, length))


def alphanumeric_generator(length, rep):
    if rep:
        return ''.join(random.choice(string.hexdigits) for _ in range(length))
    else:
        return ''.join(random.sample(string.hexdigits, length))


def punc_string_generator(length, rep):
    if rep:
        return ''.join(random.choice('$%&*+<=>@') for _ in range(length))
    else:
        return ''.join(random.sample('$%&*+<=>@', length))


def all_chars_string_generator(length, rep):
    if rep:
        return ''.join(random.choice(string.printable) for _ in range(length))
    else:
        return ''.join(random.sample(string.printable, length))


def English_word_generator():
    return random.choice(open("smaller_words.txt").read().split())


def palindrome_generator():
    return random.choice(open("palindromes.txt").read().splitlines())


def anagram_generator(input_string):
    n = len(input_string) // 2
    for _ in range(n):
        index_ = random.randint(0, len(input_string) - 1)
        random_char = input_string[index_]
        temp_string = input_string.replace(random_char, "", 1)
        index__ = random.randint(0, len(temp_string) - 1)
        input_string = temp_string[:index__] + random_char + temp_string[index__:]

    return input_string


def obj_generator():
    option = random.randint(1, 5)
    if option == 1:
        return medium_int_generator('')
    elif option == 2:
        return float_generator('')
    elif option == 3:
        return letters_string_generator(1, False)
    elif option == 4:
        return punc_string_generator(1, False)
    else:
        return English_word_generator()


def matrix_generator(t):
    rows, columns = random.randint(1, 10), random.randint(1, 10)
    ls = []
    for i in range(rows):
        ls.append([])
        if t == 'int':
            for j in range(columns):
                ls[i].append(medium_int_generator(''))
        elif t == 'float':
            for j in range(columns):
                ls[i].append(float_generator(''))
        elif t == 'obj':
            for j in range(columns):
                ls[i].append(obj_generator())
    return ls
