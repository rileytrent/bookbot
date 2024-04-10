def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    words = file_contents.split()
    counter = 0 
    for i in words:
        counter += 1 
    print(f"{counter} words in file")

if __name__ == '__main__':
    main()
