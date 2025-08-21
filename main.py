import sys
from stats import word_count, character_count, letter_sort

def get_book_text(filepath):
    filepath = str(filepath)
    with open(filepath) as f:
        return f.read()

def main():

    if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
    else:
        num_words = word_count(get_book_text(sys.argv[1]))
    #print(f"{num_words} words found in the document")
    char_dict = character_count(get_book_text(sys.argv[1]))
    #print(char_dict)

    sorted_list = letter_sort(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char in sorted_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")

main()


