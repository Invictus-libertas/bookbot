def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]

    from stats import word_count
    from stats import character_count
    from stats import presentation

    count = word_count(f"{book}")

    print(f"""============ BOOKBOT ============
    Analyzing book found at {book}
    ----------- Word Count ----------
    Found {count} total words
    --------- Character Count -------""")

    for item in presentation(character_count(f"{book}")):
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()