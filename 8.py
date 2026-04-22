#LIBRARY.py
books=[]
issued_books=[]

# !ADD BOOKS
def add_books():
    name=input("Enter book name: ")
    books.append(name)
    print("Books Added")
    
#!SHOW BOOKS  
def show_books():
    if len(books)==0:
        print("No Books Available")
    else:
        print("Books Available: ")
        for b in books:
            print(b)

#!ISSUE BOOKS
def issue_books():
    name=input("Enter book name: ")
    if name in books:
        books.remove(name)
        issued_books.append(name)
        print("Book Issued")        
    else:
        print("Book Not issued")   
        
#RETURN BOOKS
def return_books():
    name=input("Enter book name: ")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print("Books Returned")        
    else:
        print("Books Not Returned")                   
    
#? MAIN BODY

def library():
    while True:
        print("1. Add books")
        print("2.Show books")
        print("3.Issue books")
        print("4.Return books")
        print("5.Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()        
        elif choice == 3:
            issue_books()       
        elif choice == 4:
            return_books()
        elif choice == 5:
            print("Thank You")
            break         
        else:
            print("Invalid choice")
            
library()            
