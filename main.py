def main():
#    book_as_string = get_book_text("frankenstein")
    from stats import word_count
    count = word_count("frankenstein")
    from stats import character_count
    from stats import presentation
    print("============ BOOKBOT ============ \n" \
    "Analyzing book found at books/frankenstein.txt...")
#    print(character_count("frankenstein"))
    print("----------- Word Count ---------- \n" \
    f"Found {count} total words")
    print("--------- Character Count -------")
    for item in presentation(character_count("frankenstein")):
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()