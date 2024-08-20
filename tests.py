from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

@pytest.mark.parametrize('book_name', ['К', 'КоллекционерКоллекционерКоллекционерКолл'])
def test_add_new_book_add_new_book_to_collection(book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    assert book_name in collector.get_books_genre()

@pytest.mark.parametrize('book_name, genre',
                         [
                             ['Коллекционер', 'Ужасы'],
                             ['Уровень','Фантастика']
                         ]
                         )
def test_set_book_genre_set_the_genre_of_the_book(book_name, genre):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == genre

def test_get_book_genre_the_genre_corresponds_to_the_book():
    collector = BooksCollector()
    book_name = 'Под куполом'
    genre = 'Ужасы'
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == genre

@pytest.mark.parametrize('genre, book_name',
                         [
                             ['Ужасы', 'Под куполом'],
                             ['Фантастика', 'Уровень']
                         ]
                         )
def test_get_books_with_specific_genre_getting_books_of_certain_genre(genre, book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_books_with_specific_genre(genre) == [book_name]


def test_get_books_genre_dictionary_output():
    collector = BooksCollector()
    collector.add_new_book('Под куполом')
    collector.set_book_genre('Под куполом', 'Ужасы')
    output = {'Под куполом': 'Ужасы'}
    assert collector.get_books_genre() == output



def test_get_books_for_children_age_restricted_books():
    collector = BooksCollector()
    collector.add_new_book('Под куполом')
    collector.set_book_genre('Под куполом', 'Ужасы')
    books_for_children = collector.get_books_for_children()
    assert 'Под куполом' not in books_for_children

def test_get_books_for_children_books_has_no_age_restrictions():
    collector = BooksCollector()
    collector.add_new_book('Уровень')
    collector.set_book_genre('Уровень', 'Фантастика')
    books_for_children = collector.get_books_for_children()
    assert 'Уровень' in books_for_children

def test_add_book_in_favorites_the_book_is_in_favorites():
    collector = BooksCollector()
    book_name = 'Под куполом'
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    assert book_name in collector.get_list_of_favorites_books()


def test_delete_book_from_favorites_book_is_deleted_from_favorites():
    collector = BooksCollector()
    book_name = 'Под куполом'
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    collector.delete_book_from_favorites(book_name)
    assert book_name not in collector.get_list_of_favorites_books()


def test_get_list_of_favorites_books_getting_a_list_of_favorite_books():
    collector = BooksCollector()
    book_name = 'Под куполом'
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    assert book_name in collector.get_list_of_favorites_books()

