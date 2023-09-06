# qa_python
test_add_new_book_add_two_books - добавление двух новых книг. 
Проверка: вызываем get_books_genre и считаем количество элементов

test_add_new_book_add_duplicate_book - добавление одной и той же новой книги дважды. 
Проверка: вызываем get_books_genre и считаем количество элементов

test_add_new_book_name_not_match_requirements - добавление новой книги с именем не соответсвующим требованиям (слишком длинное и короткое). 
Проверка: проверяем отсутсвие в books_genre

test_set_book_genre_existing_book - присвоение допустимого жанра предварительно добавленной в books_genre новой книги. 
Проверка: в books_genre смотрим жанр по имени книги

test_set_book_genre_nonexisting_genre - присвоение недопустимого жанра, предварительно добавленной в books_genre новой книги. 
Проверка: в books_genre смотрим пустой (") жанр по имени книги

test_get_book_genre_existing_genre - добавляем новую книгу, присваиваем жанр. 
Проверка: сопоставляем присвоенный жанр с тем что вернет get_book_genre

test_get_books_with_specific_genre_existing_genre - добавляем три новые книги, двум из них присваиваем жанр. 
Проверка: имена книг с жанром сопоставляем с результатом get_books_with_specific_genre

test_get_books_genre_two_books_with_different_genre - добавляем две новые книги, присваиваем им разные жанры.
Проверка: books_genre сопоставляем с результатом get_books_genre

test_get_books_for_children_add_two_return_one - добавляем две новые книги, одной присваиваем жанр не из genre_age_rating
Проверка: книгу с жанром не из genre_age_rating сопоставляем с результатом get_books_for_children

test_add_book_in_favorites_add_existing_book_two_times - добавляем новую книгу, затем дважды добавляем ее в избранное
Проверка: количество элементов в favorites равно одному

test_delete_book_from_favorites_add_then_remove - добавляем новую книгу, добавляем ее в избранное, затем удаляем из избранного
Проверка: количество элементов в favorites равно нулю

test_get_list_of_favorites_books_one_existing_favorite - добавляем новую книгу, добавляем ее в избранное
Проверка: имя книги сопоставляем с результатом get_list_of_favorites_books