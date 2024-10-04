class Book:
  def __init__(self,title,author,is_checked_out):
    self.title = title
    self.author = author
    self._is_checked_out = is_checked_out
  def CheckOut(self):
    pass
  def ReturnBook(self):
    pass
class Library(Book):
  def __init__(self,title,author,books=None):
    super.__init__(self,title,author)
    if books is None:
     self._books = []
    else:
      self._books = books
  def add_book(self,books):
   if books.title not in self.title:
     self._books.append(books)
  def check_out_title(self,title):
    self.title =title
  def return_book(self,title):
    pass
  def list_available_books(self):
    pass
    
    
