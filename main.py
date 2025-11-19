def get_book_text(file_path):
    with open(file_path) as f:
        # do something with f (the file) here
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    words = text.split()
    return len(words)

book_text = get_book_text("books/frankenstein.txt")
word_count = get_word_count(book_text)
print(f"Found {word_count} total words.")