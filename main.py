from stats import get_word_count
from stats import get_character_count

def get_book_text(file_path):
    with open(file_path) as f:
        # do something with f (the file) here
        file_contents = f.read()
    return file_contents

book_text = get_book_text("books/frankenstein.txt")
word_count = get_word_count(book_text)
print(f"Found {word_count} total words.")

character_count = get_character_count(book_text)
print("Character counts:")
for ch, count in character_count.items():
    print(f"'{ch}': {count}")