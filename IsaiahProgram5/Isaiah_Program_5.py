#Isaiah Wolf 4-22-24
#Isaiah_Program_5.py

def displayMenu():
    print("Enter 1 to display the unique words")
    print("Enter 2 to display the words that appear in both files")
    print("Enter 3 to display the words that only appear in the first file")
    print("Enter 4 to display the words that only appear in the second file")
    print("Enter 5 to display unique words in either the first or second files but not in both")
    print("Enter 6 to exit")

def get_unique_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return set(words)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return set()
    
def display_unique_words(file1, file2):
    unique_words_file1 = get_unique_words(file1)
    unique_words_file2 = get_unique_words(file2)
    print("\nUnique words in", file1, ":\n", unique_words_file1)
    print("\nUnique words in", file2, ":\n", unique_words_file2)

def display_common_words(file1, file2):
    words_file1 = get_unique_words(file1)
    words_file2 = get_unique_words(file2)
    common_words = words_file1.intersection(words_file2)
    print("\nWords that appear in both files:\n", common_words)

def display_unique_words_file1(file1, file2):
    unique_words_file1 = get_unique_words(file1)
    words_file2 = get_unique_words(file2)
    unique_words = unique_words_file1.difference(words_file2)
    print("\nWords that only appear in the first file:\n", unique_words)

def display_unique_words_file2(file1, file2):
    words_file1 = get_unique_words(file1)
    unique_words_file2 = get_unique_words(file2)
    unique_words = unique_words_file2.difference(words_file1)
    print("\nWords that only appear in the second file:\n", unique_words)

def display_unique_words_either(file1, file2):
    unique_words_file1 = get_unique_words(file1)
    unique_words_file2 = get_unique_words(file2)
    unique_words = unique_words_file1.symmetric_difference(unique_words_file2)
    print("\nUnique words in either the first or second files but not in both:\n", unique_words)
    
def main():
    while True:
        displayMenu()
        choice = input('Enter your choice: ')

        if choice == '1':
            file1 = input("Enter the name of the first text file: ")
            file2 = input("Enter the name of the second text file: ")
            display_unique_words(file1, file2)
        elif choice == '2':
            file1 = input("Enter the name of the first text file: ")
            file2 = input("Enter the name of the second text file: ")
            display_common_words(file1, file2)
        elif choice == '3':
            file1 = input("Enter the name of the first text file: ")
            file2 = input("Enter the name of the second text file: ")
            display_unique_words_file1(file1, file2)
        elif choice == '4':
            file1 = input("Enter the name of the first text file: ")
            file2 = input("Enter the name of the second text file: ")
            display_unique_words_file2(file1, file2)
        elif choice == '5':
            file1 = input("Enter the name of the first text file: ")
            file2 = input("Enter the name of the second text file: ")
            display_unique_words_either(file1, file2)
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
