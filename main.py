def fetch_book_content(book_path):
    with open(book_path) as f:
        return f.read()


def count_book_words(content):
    words = content.split()
    print(len(words))


def main():
    book_content = fetch_book_content("books/frankenstein.txt")
    # print_book("books/frankenstein.txt")
    count_book_words(book_content)


main()
