import types

def niccolum_flatten(array):
    new_array = array[:]
    ind = 0
    while True:
        try:
            while isinstance(new_array[ind], list):
                item = new_array.pop(ind)
                for inner_item in reversed(item):
                    new_array.insert(ind, inner_item)
            ind += 1
        except IndexError:
            break
    return new_array


def flat_generator(list_of_list):
    items = niccolum_flatten(list_of_list)
    for item in items:
        yield item

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()