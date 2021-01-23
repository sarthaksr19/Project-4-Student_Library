## Library class

class Library:
    def __init__(self,listOfBooks):                 #constructor to instanciate the object.
        self.books = listOfBooks

    def displayAvailableBooks(self):                ## add library function to display the books list
        print("Books in the library are: ")
        for index,book in enumerate(self.books):    #using enumerate function to print the index as well as name of the books in the list.
            index += 1
            print(index,book)

    def borrowBook(self,bookName):                  ## add function to borrow the book
        if bookName in self.books:                  ##checking the condtion where book is available in the list or not.
            print(f"You have been issued {bookName}. Please keept it safe and return it within 30 days")
            self.books.remove(bookName)             ## removing the book name which is being issued.
            return True
        else:                                       ## if book is already being issued then this block of code will run.
            print("Sorry! this book is already been issued to some. Please try again after someday!")
            return False

    def returnBook(self,bookName):                  ##function for returning the book
        self.books.append(bookName)                 ## add book in the list when student is returnrd the book.
        print(f"Thank You!! You have successfully returned {bookName}")

## Student class

class Student:
    def requestBook(self):
        self.book = input("Enter the name of a book you want: ")
        return self.book                            ## Return self.book value in bookName argument which is in borrowBook function.

    def returnBook(self):
        self.book = input("Enter the book name you want to return: ")
        return self.book                            ## Return self.book value in bookName argument which is in returnwBook function.

##insantance the object

centralLibrary = Library(["Python","Algorithms","JavaScipts","Html","DSA in Python"])   
student = Student()

## Menu driven
while(True):
    greetmsg = ''' * * * * * WELOCOME TO CENTRAL LIBRARY * * * * *
        Please Choose an Action:
        Press 1 for List all the Books
        Press 2 for Requesting a Book
        Press 3 for Return/Add a Book
        Press 4 To Exit the Library'''
    print(greetmsg)
    try:

        a = int(input("Enter the Action: "))

        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())  # here borrowBook takes an argument of the student class requestBook function
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())   ## same here takes returnBook argumennt.
        elif a == 4:
            print("Thanks for Visting!!! Have a Nice Day.")
            exit()
            
        else:
            print("You Entered a wrong choice. Please Choose Correct Action")

    except ValueError as e:
        print("You Entered a Wrong Choice.")




