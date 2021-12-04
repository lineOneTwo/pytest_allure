import pytest


# 待测函数
def add(a, b):
    return a + b


# 多个参数的情况
@pytest.mark.parametrize('a, b, c', [(1, 2, 3), (4, 5, 9), ('1', '2', '3')])
def test_add(a, b, c):
    print(f'\na,b,c的值:{a},{b},{c}')
    print('{0}+{1}={2}'.format(a, b, add(a, b)))
    assert add(a, b) == c


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'tes_add.py'])
