'''Given a Book class and a Solution class, write a MyBook class that does the following:

Inherits from Book
Has a parameterized constructor taking these 3 parameters:
string title
string author
int price

Sample Input

The following input from stdin is handled by the locked stub code in your editor:

The Alchemist
Paulo Coelho
248
'''

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
class MyBook(Book):
    def __init__(self, title, author, price):
        super(Book, self).__init__()
            
    def display(self):
        print ('Title: ' + title)
        print ('Author: ' + author)
        print ('Price: ' + str(price))
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()