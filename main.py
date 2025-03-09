def get_book_text(path_to_file):
    #Reads the book file
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    # core functions
    # First, call get_book_text and utilize the file path. 
    # Second - call the return of get_book_text as the input to word count
    # print the return from word_count
    from stats import word_count
    from stats import count_characters
    from stats import sort
    import sys

    # sys.argv[0] is the script name
    # sys.argv[1] is the path to the book file
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]


    
    text = get_book_text(path_to_file)
    count = word_count(text)
    out = count_characters(text)
    set_list = sort(out)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for data in set_list:
        char = data["char"]
        count = data["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()