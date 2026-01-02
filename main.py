from stats import get_num_words, create_output
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    #Input validation
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_location = sys.argv[1]
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