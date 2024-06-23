def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(get_num_words(text))

# count words in a text
def get_num_words(text):
    words = text.split()
    return len(words)

# read book text from a file path
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()