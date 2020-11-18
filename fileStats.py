def main():
    filename = input("Enter the name of the file: ")
    while(True):
        try:
            fhand = open(filename, 'r')
            break
        except:
            print("File cannot be opened: ", filename)
            filename = input("Please enter a valid file name: ")
    
    lines = fhand.readlines()
    fhand.close()
    word_count = 0
    char_count = 0
    
    for line in lines:
        words = line.strip().split()
        word_count = word_count + len(words)
        for word in words:
            char_count = char_count + len(word)
    
    average = char_count/word_count
    print("Number of lines: ", len(lines))
    print("Number of words: ", word_count)
    print("Number of characters: ", char_count)
    print("Average length of word: ", average)
    

if __name__ == "__main__":
    main()
    
    