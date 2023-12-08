import pytest


@pytest.fixture()
def set_up():
    """ Предварительные действия перед выполнением основных тестов """
    print('set to account')
    """yield нужен для того что бы выйти из учетки """
    yield
    print('exit io system')


@pytest.fixture(scope='function')
def same():
    """ функция оборачивает все тесты где передана данная функция"""
    print('star')
    yield
    print('end')
