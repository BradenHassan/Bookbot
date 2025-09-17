
def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def get_number_words(text):
    return len(text.split())

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_number_words(text)
    print(f"{num_words} words found in the document")

main()