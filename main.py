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
    path_to_file = "/home/k8s/bookbot/books/frankenstein.txt"
    text = get_book_text(path_to_file)
    count = word_count(text)
    out = count_characters(text)
    set_list = sort(out)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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