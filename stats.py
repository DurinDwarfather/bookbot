
def word_count(get_book_text):
    # takes the book file and counts the words based on white space
    num_words = 0
    countable_Text = get_book_text.split()
    return len(countable_Text)

def count_characters(get_book_text):
    # This function will take the full book text as input and count each
    # instance of a character. 
    alpha = {}
    text = get_book_text.lower()
    for i in text:
        if i not in alpha:
            alpha[i] = 0
        alpha[i] += 1
    return(alpha)

def sort(count_characters):
    char_list = []
    for char, count in count_characters.items():
        char_list.append({"char" : char, "count" : count})
    
    char_list.sort(key=lambda item: item["count"], reverse=True)
    
    return char_list