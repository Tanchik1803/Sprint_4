from conftest import collector
import pytest

from main import BooksCollector

class TestBook:

    def test_add_new_book(self, collector):
        #Добавление новой книги
        collector.add_new_book('Капитанская дочка')
        assert 'Капитанская дочка' in collector.get_books_genre()

    def test_add_new_book_name_is_long(self, collector):
        #Проверка на добавление книги, у которой название длиннее 40 символов"""
        collector.add_new_book('Это очень длинное название книги, название, которой длинее сорока символов')
        assert 'Это очень длинное название книги, название, которой длинее сорока символов' not in collector.get_books_genre()


    def test_add_new_book_twice_exists(self, collector):
        #Проверка, что нельзя добавить книгу с одинаковым названием дважды
        collector.add_new_book('Марсианские рассказы')
        collector.add_new_book('Марсианские рассказы')
        count_books = len(collector.get_books_genre())
        assert count_books == 1

    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Хоббит, туда и обратно', 'Фантастика'],
                                 ['Пила', 'Ужасы'],
                                 ['Колобок', 'Мультфильмы'],
                                 ['Шерлок Холмс', 'Детективы'],
                                 ['Золотой ключик', 'Мультфильмы'],
                                 ['Любовь и голуби', 'Комедии']
                             ]
                             )

    def test_set_book_genre_success(self, collector):  
        #Проверка на добавление книги с валидным жанром
        collector.add_new_book('Любовь и голуби')
        collector.set_book_genre('Любовь и голуби', 'Комедии')
        assert collector.books_genre['Любовь и голуби'] == 'Комедии'  


    def test_set_book_genre_invalid_genre(self, collector):  
        #Проверка на добавление книги с невалидным жанром
        collector.add_new_book('Кортик')
        collector.set_book_genre('Кортик', 'Приключения')
        assert collector.books_genre['Кортик'] == ''


    def test_get_books_with_specific_genre_success(self):
        #Проверка, что возвращается список книг определенного жанра
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Шерлок Холмс'] 


    def test_add_book_in_favorites(self, collector):
        #Проверка, что книга входит в избранное
        collector.add_new_book('Любовь и голуби')
        collector.add_book_in_favorites('Любовь и голуби')
        assert 'Любовь и голуби' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        #Проверка, что книга удаляется из списка избранных книг"""
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        collector.add_book_in_favorites('Колобок')
        collector.delete_book_from_favorites('Колобок')
        assert 'Колобок' not in collector.get_list_of_favorites_books()
    
    def test_get_books_for_children(self, ):
        #Проверка, что возвращается список книг, подходящих для детей"""
        collector.add_new_book('Любовь и голуби')
        collector.set_book_genre('Любовь и голуби', 'Комедии')
        collector.add_new_book('Золотой ключик')
        collector.set_book_genre('Золотой ключик', 'Мультфильмы')
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Золотой ключик', 'Колобок']
   

    def test_get_book_genre_exists_with_genre(self, collector):
        #Проверка на получение жанра книги с установленным жанром
        collector.add_new_book('Хоббит, туда и обратно')
        collector.set_book_genre('Хоббит, туда и обратно', 'Фантастика')
        genre = collector.get_book_genre('Хоббит, туда и обратно')
        assert genre == 'Фантастика'

     def test_get_books_genre(self, collector):  
        #Проверка, что get_books_genre() возвращает словарь с корректными жанрами книг.
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_books_genre() == {'Шерлок Холмс': 'Детективы'}

    def test_get_book_genre_not_add (self, collector):
        #Проверка, если жанр книги не установлен, то вернется None
        assert collector.get_book_genre('Собачья жизнь') is None