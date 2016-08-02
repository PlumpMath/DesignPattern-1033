from abc import ABCMeta, abstractmethod

class Book():
  def __init__(self, name):
    self.name = name

  def getName(self):
    return self.name


class Aggregate(metaclass = ABCMeta):
  @abstractmethod
  def iterator(self):
    pass


class BookShelf(Aggregate):
  def __init__(self):
    self.__books = []

  def getBookAt(self, index):
    return self.__books[index]

  def appendBook(self, book):
    self.__books.append(book)

  def getLength(self):
    return len(self.__books)

  def iterator(self):
    return BookShelfIterator(self)


class Iterator(metaclass = ABCMeta):
  @abstractmethod
  def hasNext(self):
    pass

  @abstractmethod
  def next(self):
    pass


class BookShelfIterator(Iterator):
  __index = 0
  def __init__(self, bookShelf):
    self.__bookShelf = bookShelf

  def hasNext(self):
    if self.__index < self.__bookShelf.getLength():
      return True
    else:
      return False

  def next(self):
    book = self.__bookShelf.getBookAt(self.__index)
    self.__index += 1
    return book

    
if __name__ == '__main__':
  bookShelf = BookShelf()
  bookShelf.appendBook(Book('Around the World in 80 Days'))
  bookShelf.appendBook(Book('Bible'))
  bookShelf.appendBook(Book('Cinderella'))
  bookShelf.appendBook(Book('Daddy-Long-Legs'))
  it = bookShelf.iterator()
  while it.hasNext():
    book = it.next()
    print(book.getName())

