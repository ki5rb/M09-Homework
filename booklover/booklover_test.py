from booklover import BookLover
import pandas as pd
import unittest

class BookLoverTestSuite(unittest.TestCase): 
    
    def test_1_add_book(self):
         # add a book that does not exist in 'book_list':
        myinstance = BookLover("Karunya","ki5rb@virginia.edu","Fiction")
        myinstance.add_book('Lord of the Rings', 3)
        self.assertTrue(myinstance.has_read('Lord of the Rings'))

    def test_2_add_book(self):
         # add the same book twice. Test if it's in `book_list` only once.
        myinstance = BookLover("Karunya","ki5rb@virginia.edu","Fiction")
        myinstance.add_book('Charlottes Web',4)
        myinstance.add_book('Charlottes Web',4)
        unique_books = myinstance.book_list['book_name'].unique()
        expected_unique_books = ['Charlottes Web']
        self.assertCountEqual(unique_books, expected_unique_books)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        myinstance = BookLover("Karunya","ki5rb@virginia.edu","Fiction")
        myinstance.add_book('Harry Potter',5)
        self.assertTrue(myinstance.has_read('Harry Potter'))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        myinstance = BookLover("Karunya","ki5rb@virginia.edu","Fiction")
        self.assertFalse('Sherlock Holmes' in myinstance.book_list['book_name'])

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        myinstance = BookLover("Karunya","ki5rb@virginia.edu","Fiction")
        myinstance.add_book('Series of Unfortunate Events',4)
        myinstance.add_book('Handmaids Tale',2)
        myinstance.add_book('Life of Pi',5)
        expected = 3
        self.assertEqual(myinstance.num_books, expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        myinstance = BookLover("Karunya","ki5rb@virginia.edu","Fiction")
        myinstance.add_book('Nickel Boys', 2)
        myinstance.add_book('Little Fires Everywhere', 5)
        faves = myinstance.fave_books()
        expected = faves[faves['book_rating']>3]
        self.assertEqual(len(faves), len(expected)) 

if __name__ == '__main__':

    unittest.main(verbosity=3)
