import pytest

"""@pytest.mark.run() изменение очередности выполнения тестов """


@pytest.mark.run(order=5)
def test_method_1():
    print('test_method_1')


@pytest.mark.run(order=3)
def test_method_2():
    print('test_method_2')


@pytest.mark.run(order=4)
def test_method_3():
    print('test_method_3')


@pytest.mark.run(order=2)
def test_method_4():
    print('test_method_4')


@pytest.mark.run(order=1)
def test_method_5():
    print('test_method_5')
