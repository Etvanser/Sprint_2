from main import BooksCollector

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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Проверяем добавление одной книги
    def test_add_new_book_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        books_list = collector.get_books_rating()
        assert ('Властелин колец', 1) in books_list.items()

    # Проверяем что, нельзя добавить одну и ту же книгу дважды.
    def test_add_new_book_double_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        assert collector.add_new_book('Властелин колец') == None

    # Проверяем что, нельзя выставить рейтинг книге, которой нет в списке.
    def test_set_book_rating_not_in_books_rating(self):
        collector = BooksCollector()
        assert collector.set_book_rating('Властелин колец', 5) == None

    # Проверяем что, нельзя выставить рейтинг меньше 1.
    def test_set_book_rating_less_1(self):
        collector = BooksCollector()
        assert collector.set_book_rating('Властелин колец', 0) == None

    # Проверяем что, нельзя выставить рейтинг выше 10
    def test_set_book_rating_more_10(self):
        collector = BooksCollector()
        assert collector.set_book_rating('Властелин колец', 11) == None

    # Проверяем получение рейтинга по имени книги
    def test_get_book_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_rating('Властелин колец', 5)
        assert collector.get_book_rating('Властелин колец') == 5

    # Проверяем вывод списка книг по определенному рейтенгу
    def test_get_books_with_specific_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Звездные войны')
        collector.set_book_rating('Властелин колец', 9)
        collector.set_book_rating('Звездные войны', 7)
        assert 'Властелин колец' in collector.get_books_with_specific_rating(9)

    # Проверяем получения словоря books_rating
    def test_get_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Звездные войны')
        books_list = collector.get_books_rating()
        assert books_list == collector.books_rating

    # Проверяем добавления книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        assert 'Властелин колец' in collector.get_list_of_favorites_books()

    # Проверяем удаление книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        collector.delete_book_from_favorites('Властелин колец')
        assert 'Властелин колец' not in collector.get_list_of_favorites_books()

    # Проверяем получение списка Избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Звездные войны')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Звездные войны')
        assert collector.get_list_of_favorites_books() == collector.favorites