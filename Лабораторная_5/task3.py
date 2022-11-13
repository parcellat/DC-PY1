import random
def get_unique_list_numbers() -> list[int]:
    l = [i for i in range(-10, 11)]
    res = []
    for _ in range(15):
        cur_num = random.choice(l)
        res.append(cur_num)
        l.remove(cur_num)
    return res
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
