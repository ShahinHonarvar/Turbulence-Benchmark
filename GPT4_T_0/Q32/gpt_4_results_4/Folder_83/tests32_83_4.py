from Q32.gpt_4_results_4.Folder_83.generated_answer import insert_after_character
import random
import string


def test_string_of_length_one():
    s = 'E'
    assert insert_after_character(s) == 'E' + 'e'


def test_large_string_of_only_specified_character():
    s = 'E' * 1000
    assert insert_after_character(s) == ('E' + 'e') * 1000


def test_length_of_large_string_of_only_specified_character():
    s = 'E' * 1000
    assert len(insert_after_character(s)) == 2 * len(s)


def test_presence_of_inserted_character():
    s = ''.join(random.choices(string.ascii_letters + string.digits + ' ' * 10, k = 1000))
    s = s + 'E'
    returned_string = insert_after_character(s)
    assert 'e' in returned_string


def test_compare_length_of_strings():
    s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    s = s + 'E'
    returned_string = insert_after_character(s)
    assert len(s) < len(returned_string)
    

def test_length_of_result():
    s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    s = s + 'E'
    returned_string = insert_after_character(s)
    count = s.count('E')
    assert len(returned_string) == len(s) + count
    

def test_first_index_of_insert_char_in_result():
    s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    s = s.replace('e', '')
    s = s.replace('E', '')
    s = 'E' + s
    returned_string = insert_after_character(s)
    if 'e' == 'E':
        assert returned_string.find('e') == 0
        assert returned_string.rfind('e') == 1
    else:
        assert returned_string.find('e') == 1


def test_all_indices_of_char_destination_in_result():
    s = ''.join(random.choices(string.ascii_letters + string.digits + ' ' * 10, k=1000))
    s = s + 'E'
    s = s.replace('e', '')
    returned_string = insert_after_character(s)
    indices_in_s = [i[0] for i in enumerate(s) if i[1] == 'E']
    indices_in_returned_string = [i[0] for i in enumerate(returned_string) if i[1] == 'e']
    length = len(indices_in_s)
    assert length == len(indices_in_returned_string)
    l = [indices_in_s[i] + i + 1 for i in range(len(indices_in_s))]
    assert l == indices_in_returned_string
