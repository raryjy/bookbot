def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word = get_book_words(book_path)
    char_dict = get_book_characters(text)
    print_char(char_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_words(path):
    text = get_book_text(path)
    return text.split()

def get_book_characters(text):
    my_dict = {}
    for char in text.lower():
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1
    return my_dict

def print_char(char_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    for key, value in char_dict.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


main()