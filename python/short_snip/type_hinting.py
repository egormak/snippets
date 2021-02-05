# Используется, что бы указать тип
def add_int(val: int):
    return val + val
add_int(2)


# Можно указать сведения об ожидаемых типах
def sum_dict(var: dict[str, int]):
    return sum(var[key] for key in var)
test = {'text': 5, 'two': 7}
test2 = {1: 5, 2: 7}

sum_dict(test)
sum_dict(test2)

def sum_dict_1(var: dict) -> int:
    return sum(var[key] for key in var)
test_1: dict = {'text': 5, 'two': 7}

sum_dict_1(test_1)
