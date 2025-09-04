import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
filepath = sys.argv[1]
from stats import get_num_words, get_char_count, sort_char_count, char_dict_to_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(filepath)
    # word count
    num_words = get_num_words(text)
    # character counts
    chars = char_dict_to_list(get_char_count(text))
    chars.sort(reverse=True, key=sort_char_count)

    # ==== Report ====
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_dict in chars:
        char = char_dict["char"]
        num = char_dict["num"]
        if char.isalpha():  # skip non-letters
            print(f"{char}: {num}")
    
    print("============= END ===============")
    
main()