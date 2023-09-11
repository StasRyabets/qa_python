from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2, "get_books_genre вернул НЕ две книги"

    def test_add_new_book_add_duplicate_book(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1, "get_books_genre вернул НЕ одну книгу"

    @pytest.mark.parametrize('book_name', ["Г" * 41, ""])
    def test_add_new_book_name_not_match_requirements(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0, "add_new_book добавил книгу с некорректным названием"
    
    def test_set_book_genre_existing_book(self):
        collector = BooksCollector()
        book_name = "Сахарный Кремль"
        genre = "Фантастика"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre, "get_book_genre вернул не тот жанр что был передан в set_book_genre"

    def test_set_book_genre_nonexisting_genre(self):
        collector = BooksCollector()
        book_name = "До третьих петухов"
        genre = "Сказка"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == '', "get_book_genre вернул не пустое значение, предположительно set_book_genre записал несуществующий жанр"

    def test_get_books_with_specific_genre_existing_genre(self):
        collector = BooksCollector()
        book_not_in_list = "Железный совет"
        first_book_in_list = "Вокзал потерянных снов"
        second_book_in_list = "Шрам"
        genre = "Детективы"
        collector.add_new_book(book_not_in_list)
        collector.add_new_book(first_book_in_list)
        collector.add_new_book(second_book_in_list)
        collector.set_book_genre(first_book_in_list, genre)
        collector.set_book_genre(second_book_in_list, genre)
        assert collector.get_books_with_specific_genre(genre) == [first_book_in_list, second_book_in_list], "get_books_with_specific_genre вернул НЕ две книги с подходящим жанром"

    def test_get_books_genre_two_books_with_different_genre(self):
        collector = BooksCollector()
        first_book = "Поиск предназначения, или Двадцать се..."
        second_book = "За закрытыми дверями"
        first_genre = "Детективы"
        second_genre = "Комедии"
        collector.add_new_book(first_book)
        collector.add_new_book(second_book)
        collector.set_book_genre(first_book, first_genre)
        collector.set_book_genre(second_book, second_genre)
        assert collector.get_books_genre() == collector.books_genre, "get_books_genre вернул не те значения что добавлялись add_new_book и set_book_genre"

    def test_get_books_for_children_add_two_return_one(self):
        collector = BooksCollector()
        book_name = "В исправительной колонии"
        book_in_list = "Маленький принц"
        genre = "Мультфильмы"
        collector.add_new_book(book_name)
        collector.add_new_book(book_in_list)
        collector.set_book_genre(book_in_list, genre)
        assert collector.get_books_for_children() == [book_in_list], "get_books_for_children отфильтровал неправильно"

    def test_add_book_in_favorites_add_existing_book_two_times(self):
        collector = BooksCollector()
        book_name = "Трое в лодке, не считая собаки"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1, "get_list_of_favorites_books вернул НЕ одну книгу"

    def test_delete_book_from_favorites_add_then_remove(self):
        collector = BooksCollector()
        book_name = "Кошмары аиста Марабу"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert collector.get_list_of_favorites_books() == [], "get_list_of_favorites_books вернул не пустой список после delete_book_from_favorites"

    def test_get_list_of_favorites_books_one_existing_favorite(self):
        collector = BooksCollector()
        book_name = "Дом листьев"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == [book_name]

