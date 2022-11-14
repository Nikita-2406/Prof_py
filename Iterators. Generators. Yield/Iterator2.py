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

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.item = niccolum_flatten(self.list_of_list)
        self.item.reverse()
        return self

    def __next__(self):
        if self.item == []:
            raise StopIteration
        else:
            return self.item.pop()


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()