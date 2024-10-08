class Book:
 def __init__(self,title,author):
  self.title = title
  self.author =author
 def __str__(self):
  return f"{self.title} by {self.author}"
class EBook(Book):
 def __init__(self,title,author,file_size):
  super().__init__(title,author)
  self.file_size = file_size
 class PrintBook(Book):
  def __init__(self,title,author,page_count):
   super().__init__(title,author)
   self.page_count = page_count
class Library:
 def __init__(self):
  self.books = []
 def add_books(self,book):
  self.books.append(book)
 def list_books(self):
  for book in self.books:
    if isinstance(book, PrintBook):
      print(f"PrintBook - Title: {book.title}, Author: {book.author}, Pages: {book.page_count}")
    elif isinstance(book, EBook):
      print(f"EBook - Title: {book.title}, Author: {book.author}, File Size: {book.file_size}MB")