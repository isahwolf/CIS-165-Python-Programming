#Isaiah Wolf 4/7/24
#Isaiah_Exam_2

def displayMenu(): #displays the menu
    print("Enter 1 to convert a string to uppercase")
    print("Enter 2 to convert a string to lowercase")
    print("Enter 3 to count the number of words in a string")
    print("Enter 4 to count the number of vowels in a string")
    print("Enter 5 to exit")

def main():
    while True:
        displayMenu()
        choice = input("Enter your choice: ")

        if choice == '5': #exits the loop
            print("Exiting...")
            break
        elif choice not in ['1', '2', '3', '4']: #doesn't allow incorrect choices
            print("Invalid choice. Please try again.")
            continue

        user_string = input("Enter a string: ")
        while len(user_string) == 0:
            print("You must enter at least one character.")
            user_string = input("Enter a string: ")

        if choice == '1': #converts the string to uppercase
            result = user_string.upper()
            print("Original string: {}\nConverted string to uppercase: {}".format(user_string, result))
        elif choice == '2': #converts the string to lowercase
            result = user_string.lower()
            print("Original string: {}\nConverted string to lowercase: {}".format(user_string, result))
        elif choice == '3': #counts the number of words in the string
            user_list = user_string.split()
            result = len(user_list)
            print("Original string: {}\nNumber of words in string: {}".format(user_string, result))
        elif choice == '4': #counts the number of vowels in the string
            vowels = 'aeiouAEIOU'
            count = 0
            for char in user_string: #examines each character in the string to determine the number of vowels
                if char in vowels:
                    count += 1
            print("Original string: {}\nNumber of vowels in string: {}".format(user_string, count))

if __name__ == "__main__":
    main()
