import sys
from stats import get_num_each_letter, organize_dict, get_number_words

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print(f"Analyzing book found at {file_path}")
    text = get_book_text(file_path)
    print("----------- Word Count ----------")
    num_words = get_number_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_letters = get_num_each_letter(text)
    for char in organize_dict(num_letters):
        print(f"{char["char"]}: {char["count"]}")
    print("============= END ===============")
main()