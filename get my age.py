import datetime

def main():
    BDD=input("Enter your BDD:")
    yearnow=datetime.datetime.now().year
    myage=yearnow-int (BDD)
    print("your age is {}".format(myage))


if __name__ == '__main__':main()
