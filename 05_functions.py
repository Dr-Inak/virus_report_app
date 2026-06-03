print('Fun Fact: print() is a function')

def summa (a,b):
    return a * b

calc = summa(3,9)

print(calc)


def test_func_01():
    test_var_01 = 10
    print(test_var_01)

test_func_01()


def outer_func():
    msg = 'Hello there!'
    res = ""

    def inner_func():
        nonlocal res
        global mr_inter_var
        mr_inter_var = 'MJ'
        res = "How Are You?"
        print(msg)

    inner_func()
    print(res)

outer_func()

print(mr_inter_var)