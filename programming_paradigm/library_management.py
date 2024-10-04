class Book:
  def __init__(self,title,author):
    self.title = title
    self.author = author
    self._is_checked_out = False
  def CheckOut(self):
# this method returns false if the book is already checked outindicating that the checkout operation was no successful
    if self._is_checked_out:
      return False
    self._is_checked_out = True
    return True
  def ReturnBook(self):
    if not self._is_checked_out:
      return False
    self._is_checked_out = False
    return True
class Library:
  def __init__(self):
    self._books = []
  def add_book(self,book):
   if book.title not in self.title:
     self._books.append(book)
  def check_out_title(self,title):
    self.title =title
  def return_book(self,title):
    pass
  def list_available_books(self):
    pass
    
    
