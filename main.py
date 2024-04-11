def main():
    text = "books/frankenstein.txt"
    with open(text) as f:
        file_contents = f.read()
    #print(file_contents)
    words = file_contents.split()
    word_counter = (len(words))
    print("")
    print(f"--- Report of {text} file ---")
    print("")
    print("---------------------------------------------")
    print("")
    print(f"This file has {word_counter} words in it.")
    print("")
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    lower_words = file_contents.lower()
    letter_count_dict = {letter: 0 for letter in english_letters}
    for char in lower_words:
        if char in english_letters:
            letter_count_dict[char] += 1
    #print(letter_count_dict)
    for key, value in letter_count_dict.items():
        print(f"The '{key}' character was found {value} times")
    print("")
    print("--------------- End of Report ---------------")
    print("")

if __name__ == '__main__':
    main()
