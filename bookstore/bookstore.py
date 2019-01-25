def create_bookstore(name):
    return {"name":name,
            "authors":{},
            "books":{}
            
            }


def get_bookstore_name(bookstore):
    return bookstore["name"]


def add_author(bookstore, name, nationality):
    author={'name':name, 'nationality':nationality}
    bookstore["authors"].setdefault(name,author)
    return bookstore["authors"][name]
   
def get_author_by_name(bookstore, name):
    return bookstore["authors"][name]


def add_book(bookstore, title, isbn, author):
    book={'title':title,'isbn':isbn,'author':author}
    bookstore['books'].setdefault(title,book)
    return (bookstore['books'][title])


def get_book_by_title(bookstore, title):
    return bookstore['books'][title]
        


def get_books_by_author(bookstore, author):
    book_list=[]
    print (bookstore)
    for book in bookstore['books'].values():
        if book['author'] == author:
            book_list.append(book)
    return book_list
