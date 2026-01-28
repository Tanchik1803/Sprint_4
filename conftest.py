import pytest

from main import BooksCollector
#Создадим фикстуру
@pytest.fixture
def collector():
    return BooksCollector()