from Q32.gpt_3_5_turbo_results_4.Folder_99.generated_answer import insert_after_character
import random
import string


def test_string_of_length_one():
    s = 'a'
    assert insert_after_character(s) == 'a' + 'W'


def test_large_string_of_only_specified_character():
    s = 'a' * 1000
    assert insert_after_character(s) == ('a' + 'W') * 1000


def test_length_of_large_string_of_only_specified_character():
    s = 'a' * 1000
    assert len(insert_after_character(s)) == 2 * len(s)


def test_presence_of_inserted_character():
    s = ''.join(random.choices(string.ascii_letters + string.digits + ' ' * 10, k = 1000))
    s = s + 'a'
    returned_string = insert_after_character(s)
    assert 'W' in returned_string


def test_compare_length_of_strings():
    s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    s = s + 'a'
    returned_string = insert_after_character(s)
    assert len(s) < len(returned_string)
    

def test_length_of_result():
    s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    s = s + 'a'
    returned_string = insert_after_character(s)
    count = s.count('a')
    assert len(returned_string) == len(s) + count
    

def test_first_index_of_insert_char_in_result():
    s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    s = s.replace('W', '')
    s = s.replace('a', '')
    s = 'a' + s
    returned_string = insert_after_character(s)
    if 'W' == 'a':
        assert returned_string.find('W') == 0
        assert returned_string.rfind('W') == 1
    else:
        assert returned_string.find('W') == 1


def test_all_indices_of_char_destination_in_result():
    s = ''.join(random.choices(string.ascii_letters + string.digits + ' ' * 10, k=1000))
    s = s + 'a'
    s = s.replace('W', '')
    returned_string = insert_after_character(s)
    indices_in_s = [i[0] for i in enumerate(s) if i[1] == 'a']
    indices_in_returned_string = [i[0] for i in enumerate(returned_string) if i[1] == 'W']
    length = len(indices_in_s)
    assert length == len(indices_in_returned_string)
    l = [indices_in_s[i] + i + 1 for i in range(len(indices_in_s))]
    assert l == indices_in_returned_string
