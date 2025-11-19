def get_book_text(file_path):
    with open(file_path) as f:
        # do something with f (the file) here
        file_contents = f.read()
    return file_contents


book_text = get_book_text("books/frankenstein.txt")
print(book_text)