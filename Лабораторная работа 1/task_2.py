# TODO Найдите количество книг, которое можно разместить на дискете

disk_volume_megabyte = 1.44
papers_in_book = 100
count_strings_in_paper = 50
count_symbols_in_string = 25
symbol_kilobyte = 4

book_volume_byte = symbol_kilobyte * count_symbols_in_string * count_strings_in_paper * papers_in_book
book_volume_megabyte = book_volume_byte / 1024 / 1024
count_books = disk_volume_megabyte // book_volume_megabyte

print("Количество книг, помещающихся на дискету:", int(count_books))
