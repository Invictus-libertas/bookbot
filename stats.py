def get_book_text(title):
    with open(f"./books/{title}.txt") as book:
        return book.read()

def word_count(title):
    book_as_string = get_book_text(title)
    count = 0
    for word in book_as_string.split():
        count += 1
    return count

def character_count(title):
    book_as_string = get_book_text(title)
    char_dict = {}
    for char in book_as_string.lower():
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def sort_on(dict):
    return dict["count"]
    
def presentation(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list

    
