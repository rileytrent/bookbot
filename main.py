def main():
    # enter a path to a file in the text variable
    text = "books/frankenstein.txt"
    with open(text) as f:
        file_contents = f.read()
    # gets the contents of the text file
    words = file_contents.split()
    # counts the words in the fild
    word_counter = (len(words))
    # formatting for the end report 
    print("")
    print(f"--- Report of {text} file ---")
    print("")
    print("---------------------------------------------")
    print("")
    print(f"This file has {word_counter} words in it.")
    print("")
    #creates a Dictionary of all the letters in the english language as the key and the frequency of each letter in the text file as the value
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    lower_words = file_contents.lower()
    letter_count_dict = {letter: 0 for letter in english_letters}
    for char in lower_words:
        if char in english_letters:
            letter_count_dict[char] += 1
    # prints every key and value in the format below 
    for key, value in letter_count_dict.items():
        print(f"The '{key}' character was found {value} times")
    print("")
    print("--------------- End of Report ---------------")
    print("")

if __name__ == '__main__':
    main()
