from stats import word_count
from stats import char_count
from stats import sort_char_count
import sys


# open and read a text file
def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return(file_content)

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    counts = char_count(book_text)
    sorted_chars = sort_char_count(counts)
    for char in sorted_chars:
        # only print alphabetic characters
        # char is a list of dictionaries
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
    
if __name__ == "__main__":
    main()