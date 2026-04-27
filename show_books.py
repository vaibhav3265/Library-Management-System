from utils import books
def show():
    if len(books)==0:   print("Book not available")
    else:
        print("Available Books are: ")
        for _ in books:
            print(_)