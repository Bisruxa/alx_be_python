class Book:
  def __init__(self,title,author,is_checked_out):
    self.title = title
    self.author = author
    self._is_checked_out = is_checked_out
class Library(Book):
  def __init__(self,books):
    self._books = books
  def add_book(self):
   self.title = Book.title
   self.author = Book.author
  def check_out_title(self,title):
    self.title =title
  def return_book(self,title):
    pass
  def list_available_books(self):
    pass
    
    
