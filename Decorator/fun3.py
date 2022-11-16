import datetime
import types
def logger(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        time = datetime.datetime.today()
        line = f'Вызвана функция {old_function.__name__} с аргументами {args} и {kwargs} с результатом {result} в {time}'
        print(line)
        return result

    return new_function


@logger
def flat_generator(list_of_lists):
    items = sum(list_of_lists, [])
    for item in items:
        yield item


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()