def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(get_chars_dict(text))

# count words in a text
def get_num_words(text):
    words = text.split()
    return len(words)

# read book text from a file path
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    lowered_text = text.lower()
    chars_dict = {}

    for char in lowered_text:
        # add char if not in dict
        if char not in chars_dict:
            chars_dict[char] = 1
        # else increase counter
        else:
            chars_dict[char] += 1
    return chars_dict

main()