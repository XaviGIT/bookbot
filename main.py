def fetch_book_content(book_path):
    with open(book_path) as f:
        return f.read()


def count_book_words(content):
    words = content.split()
    return len(words)


def count_book_letters(content):
    letters = {}
    for w in content:
        lower_w = w.lower()
        if lower_w in letters:
            letters[lower_w] += 1
        else:
            letters[lower_w] = 1
    return letters


def letters_report(book_path):
    end_line = "\r\n"
    report = f"--- Begin report of {book_path} ---{end_line}"

    book_content = fetch_book_content(book_path)
    words_count = count_book_words(book_content)
    report += f"{words_count} words found in the document{end_line}{end_line}"

    letters = count_book_letters(book_content)
    sorted_letters = dict(sorted(letters.items()))

    for l in sorted_letters:
        if l.isalpha():
            report += f"The '{l}' character was found {letters[l]} times{end_line}"

    report += "--- End report ---"
    return report


def main():
    # book_content = fetch_book_content("books/frankenstein.txt")
    # print book content
    # print_book("books/frankenstein.txt")
    # print book words count
    # print(count_book_words(book_content))
    # print book letters counts
    # print(count_book_letters(book_content))
    # print book letters counts report
    # letters = count_book_letters(book_content)
    print(letters_report("books/frankenstein.txt"))


main()
