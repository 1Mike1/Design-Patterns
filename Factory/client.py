from factory import Factory

def main():
    user_input = str(input("Enter OS Name[Android/IOS]:"))
    f_os = Factory.create_instance(user_input)
    if f_os:
        print(f_os.specs())
    else:
        print("Sorry we dont have information about this os.")

if __name__ == '__main__':
    main()
    