from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        assert len(collector.get_books_rating()) == 1

    def test_add_new_book_double_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Властелин колец')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_not_in_books_rating(self):
        collector = BooksCollector()
        collector.set_book_rating('Властелин колец', 5)
        assert collector.get_book_rating('Властелин колец') != 5

    def test_set_book_rating_less_1(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_rating('Властелин колец', 0)
        assert collector.get_book_rating('Властелин колец') == 1

    def test_set_book_rating_more_10(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_rating('Властелин колец', 11)
        assert collector.get_book_rating('Властелин колец') == 1

    def test_get_book_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_rating('Властелин колец', 5)
        assert collector.get_book_rating('Властелин колец') == 5

    def test_get_books_with_specific_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Звездные войны')
        collector.set_book_rating('Властелин колец', 9)
        collector.set_book_rating('Звездные войны', 7)
        assert 'Властелин колец' in collector.get_books_with_specific_rating(9)

    def test_get_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Звездные войны')
        assert 'Властелин колец' and 'Звездные войны' in collector.get_books_rating()

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        assert 'Властелин колец' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        collector.delete_book_from_favorites('Властелин колец')
        assert 'Властелин колец' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Звездные войны')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Звездные войны')
        assert 'Властелин колец' and 'Звездные войны' in collector.get_list_of_favorites_books()