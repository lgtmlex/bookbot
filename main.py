def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    letter_count_list = convert_dict_to_list(letter_count)
    report = generate_report(book_path, word_count, letter_count_list)
    print(report)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    total_words = text.split()
    return len(total_words)

def count_letters(text):
    chars = {}
    for letter in text:
        lowercaseLetter = letter.lower()
        if lowercaseLetter in chars:
            chars[lowercaseLetter] += 1
        else:
            chars[lowercaseLetter] = 1
    return chars

def convert_dict_to_list(dict):
    list = []
    for el in dict:
        list.append({"name": el, "num": dict[el]})
    return list

def sort_on(dict):
    return dict["num"]

def generate_report(book_path, word_count, letter_count_list):
    letter_count_list.sort(reverse=True, key=sort_on)
    heading_string = f"--- Begin report of {book_path} ---\n"
    word_count_string = f"{word_count} words found in the document\n"
    main_string = "\n"
    for letter_count in letter_count_list:
        if letter_count["name"].isalpha():
            appened_string = f"The '{letter_count["name"]}' was found {letter_count["num"]} times\n"
            main_string = main_string + appened_string
    ending_string = "--- End report ---\n"
    report_string = heading_string + word_count_string + main_string + ending_string
    return report_string
main()