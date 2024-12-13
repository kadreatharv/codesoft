print("---------------------PASSWORD GENERATOR---------------------")
import random
import string

def genrate_password(lenght):
    all_character = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(all_character) for _ in range(lenght))
    return password

def main():
    while True:
        try:
            lenght = int(input("Enter the desierd lenght of your Password:"))
            if lenght < 4:
                print("The lenght should be atlest 4 character")
            else:
                break
        except ValueError:
            print("invalid lenght")
    password = genrate_password(lenght)
    print(f"your Genreated Password is {password}")

if __name__ == "__main__":
    main()

