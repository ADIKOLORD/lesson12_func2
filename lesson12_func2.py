# Problem 1
"""
def all_math(a: int, b: int, s='+'):
    try:
        return eval(f'{a}{s}{b}')
    except ZeroDivisionError:
        return 'ERROR'
print(all_math(15, 0, '/'))
"""

# Problem 2
"""
def mylen(text: str):
    count = 0
    for i in text:
        count += 1
    return count
print(mylen('Adilet')) # >= 6
"""

# Problem 3
"""
def add_dict(first: dict, second: dict):
    first.update(second)
    return first
"""

# Problem 5
"""
def create_file(name_file):
    with open(f'{name_file}.txt' , 'w') as f:
        pass
create_file('Adiko')
"""

# Problem 1
"""
def main_func():
    print("I'm main function")
    def in_func():
        print("I'm inner function")
    in_func()
main_func()
"""

# Problem 2
"""
def conver_tuple(dict: dict):
    keys = tuple(dict.keys())
    values = tuple(dict.values())
    return keys, values
"""

# Problem 3
"""
def prostoi(number: int):
    if number == 2:
        return True
    else:
        pros = True
        for i in range(2, int((number+5) / 2)):
            if number % i == 0:
                pros = False
    return pros
"""

# Problem 1
"""
def get_list(first, second):
    return [first, second]
"""

# Problem 2
"""
def int_str(num):
    return f'{num}\n' * int(num)
print(int_str(5))
"""

# Problem 3
"""
def name_money(name, money=5000):
    return f'{name} - {money}'
"""

# Problem 4
"""
def get_rand(num:int):
    l = [str(i) for i in range(num * 3)]
    return list(set(l[:num]))
"""
