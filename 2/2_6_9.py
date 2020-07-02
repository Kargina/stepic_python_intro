from collections import namedtuple
from collections import defaultdict
import functools

recipes = {'Бутерброд с ветчиной': {'Хлеб': 50, 'Ветчина': 20, 'Сыр': 20},
           'Салат Витаминный': {'Помидоры': 50, 'Огурцы': 20, 'Лук': 20, 'Майонез': 50, 'Зелень': 20}}

store = {'Хлеб': 250, 'Ветчина': 120, 'Сыр': 120,
         'Помидоры': 50, 'Огурцы': 20, 'Лук': 20,
         'Майонез': 50, 'Зелень': 20}

statistics = defaultdict(list)
Order = namedtuple('Order', ['success', 'portions'])


def collect_statistics(statistics):
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            if result[0] == 0:
                portions_num = args[1]-result[1]
            else:
                portions_num = args[1]
            statistics[args[0]].append(Order(success=result[0], portions=portions_num))
            return result
        return wrapped
    return decorator


@collect_statistics(statistics)
def check_portions(food, count, recipes=recipes, store=store):
    if food not in recipes:
        return 0, 0

    food_for_recipe = recipes[food]
    max_num = float("inf")

    for k, v in food_for_recipe.items():
        if k not in store:
            return 0, 0
        food_num = store[k] // v
        max_num = food_num if max_num > food_num else max_num

    if max_num >= count:
        return 1, count
    return 0, max_num
