def count_words(filename):
    try:
        
        with open(filename, "r") as file:
            
            content = file.read()
           
            words = content.split()
            
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def main():
    filename = "/home/hp/Skillohomework/homework_5/homework9/words.txt"
    word_count = count_words(filename)
    if word_count is not None:
        print(f"The file '{filename}' contains {word_count} words.")

if __name__ == "__main__":
    main()
