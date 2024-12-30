def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word = get_book_words(book_path)
    char_dict = get_book_characters(text)
    print(char_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_words(path):
    text = get_book_text(path)
    return text.split()

def get_book_characters(text):
    my_dict = {}
    for char in text:
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1
    return my_dict

main()