import os, sys

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    # a dictionary with count of chars [{'p': 1234}; {'o' : 987}; ... ]
    chars_dict = get_chars_dict(text)

    # convert your dictionary of characters into a list of dictionaries
    #chars_dict chars = get_list_of_dict(chars_dict)

    print_report(text)

# count words in a text
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    
def print_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_num_words(text)} words found in the document")
    
    chars_dict = get_chars_dict(text)

    for char in sorted(chars_dict, key=chars_dict.get, reverse=True):
        if char.isalpha():
            print(f'The "{char}" character was found {chars_dict[char]} times')

    print("--- End report ---")

# convert dictionary of characters into a list of dictionaries
#def get_list_of_dict(chars_dict):
 #   chars_list = []

  #  for item in chars_dict: 
   #     new_dict[item] = chars_dict[item]
        #print(chars_dict[item])
    #return new_dict

# read book text from a file path
def get_book_text(path):
    with open(path) as f:
        return f.read()

#print ("Current working dir : %s" % os.getcwd())
main()