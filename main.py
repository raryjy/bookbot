def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word = get_book_words(book_path)
    char_dict = get_book_characters(text)
    char_sorted_list = char_dict_to_sorted_list(char_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len (word)} words found in the document")
    print()
    print_char(char_sorted_list)
    print("--- End report ---")

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

def sort_on(d):
    return d["Count"]

def char_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"Char": char, "Count": char_dict[char]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

def print_char(char_sorted_list):
    for char in char_sorted_list:
        if char["Char"].isalpha():
            print(f"The '{char['Char']}' character was found {char['Count']} times")


main()