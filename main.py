def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word = get_book_words(book_path)
    print(len(word))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_words(path):
    text = get_book_text(path)
    return text.split()

main()