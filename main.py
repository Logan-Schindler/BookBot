from stats import get_num_words, create_output

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_location = "books/frankenstein.txt"
    text = get_book_text(book_location)
    num_words = get_num_words(text)
    sorted_char_count = create_output(text)

    output = "============ BOOKBOT ============\n"
    output += f"Analyzing book found at {book_location}...\n"
    output += "----------- Word Count ----------\n"
    output += f"Found {num_words} total words\n"
    output += "--------- Character Count -------\n"
    output += sorted_char_count
    output += "============= END ==============="

    print(output)

    

main()