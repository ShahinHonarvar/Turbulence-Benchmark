from Q30.command_results_2.Folder_61.generated_answer import insert_before_character
import random
import string


def test_string_of_length_one():
    s = 'e'
    assert insert_before_character(s) == '0' + 'e'


def test_large_string_of_only_specified_character():
    s = 'e' * 1000
    assert insert_before_character(s) == ('0' + 'e') * 1000


def test_length_of_large_string_of_only_specified_character():
    s = 'e' * 1000
    assert len(insert_before_character(s)) == 2 * len(s)
    

def test_presence_of_inserted_character():
    s = ''.join(random.choices(string.ascii_letters + string.digits + ' ' * 10, k=1000))
    s = s + 'e'
    returned_string = insert_before_character(s)
    assert '0' in returned_string


def test_compare_length_of_strings():
    s = ''.join(random.sample(string.ascii_letters + string.digits, k=20))
    s = s + 'e'
    returned_string = insert_before_character(s)
    assert len(s) < len(returned_string)
    

def test_length_of_result():
    s = ''.join(random.sample(string.ascii_letters + string.digits, k=20))
    s = s + 'e'
    returned_string = insert_before_character(s)
    count = s.count('e')
    assert len(returned_string) == len(s) + count
    

def test_first_index_of_insert_char_in_result():
    s = ''.join(random.sample(string.ascii_letters + string.digits, k=20))
    s = s + 'e'
    s = s.replace('0', '')
    returned_string = insert_before_character(s)
    assert returned_string.find('0') == s.find('e')


def test_all_indices_in_result():
    s = ''.join(random.choices(string.ascii_letters + string.digits + ' ' * 10, k=1000))
    s = s + 'e'
    s = s.replace('0', '')
    returned_string = insert_before_character(s)
    indices_in_s = [i[0] for i in enumerate(s) if i[1] == 'e']
    indices_in_returned_string = [i[0] for i in enumerate(returned_string) if i[1] == '0']
    length = len(indices_in_s)
    assert length == len(indices_in_returned_string)
    l = [indices_in_s[i] + i for i in range(len(indices_in_s))]
    assert l == indices_in_returned_string
