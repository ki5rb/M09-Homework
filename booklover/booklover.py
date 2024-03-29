
# Name:  Karunya Iyappan
# Net ID: ki5rb
# URL of this file in GitHub:

import pandas as pd
import unittest

class BookLover:

    #constructor
    def __init__(self, name, email, fav_genre):
        self.name = name # string type
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    # method 1 - add a book
    def add_book(self,book_name, book_rating):
        if book_name not in self.book_list['book_name'].values.tolist():
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print("You already have this book!")
    
    # method 2 - has read the book
    def has_read(self,book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
    
    # method 3 -number of books read
    def num_books_read(self):
        return self.num_books
    
    # method 4 - favorite books - get books from book list that have a book rating over 3 
    def fave_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
    
if __name__ == '__main__':

    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)



