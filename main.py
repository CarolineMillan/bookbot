from stats import count_words, count_chars, sort_char_count
import sys

def get_book_text(filepath):
    ## opens the file at filepath and prints the contents
    with open(filepath) as f:
        contents = f.read()
        return contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at " + sys.argv[1] + "...")
    print("----------- Word Count ----------")
    contents = get_book_text(sys.argv[1])
    num_words = count_words(contents)
    num_chars = count_chars(contents)
    sorted_chars = sort_char_count(num_chars)
    print("Found", num_words, "total words")
    print("--------- Character Count -------")
    for line in sorted_chars:
        if line['char'].isalpha():
            output = line['char'] + ": " + str(line['num'])
            print(output)

main()