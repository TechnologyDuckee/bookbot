import sys
from stats import get_word_count
from stats import get_character_count

def get_book_text(file_path):
    with open(file_path) as f:
        # do something with f (the file) here
        file_contents = f.read()
    return file_contents

def sort_on_count(item):
    return item[1]
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]

book_text = get_book_text(file_path)
word_count = get_word_count(book_text)
character_count = get_character_count(book_text)
# sort character counts by count value (dict -> list of (ch,count))
character_items = list(character_count.items())
character_items.sort(key=sort_on_count, reverse=True)

# print reports
print("============ BOOKBOT ============")
print(f"Analyzing book found at {file_path} ...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words.")
print("-------- Character Count --------")
print("Character counts:")
for ch, count in character_items:
    print(f"  {ch}: {count}")