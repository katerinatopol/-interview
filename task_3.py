"""
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения, в
словаре для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.
"""

keys_1 = ['1', '2', '3', '4', '5', '6']
val_1 = ['a', 'b', 'c']

keys_2 = ['1', '2', '3']
val_2 = ['a', 'b', 'c', 'd']


def get_dict(keys, val):
    result = {}
    if len(keys) > len(val):
        for _ in range(len(keys) - len(val)):
            val.append(None)
    elif len(keys) < len(val):
        val = val[:len(keys)]

    for ind, k in enumerate(keys):
        result.update({k: val[ind]})

    return result


def main():
    print(get_dict(keys_1, val_1))
    print(get_dict(keys_2, val_2))


if __name__ == '__main__':
    main()
