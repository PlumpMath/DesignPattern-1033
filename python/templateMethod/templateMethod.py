#! /user/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class AbstractDisplay(metaclass = ABCMeta):
  @abstractmethod
  def openChar(self):
    pass

  @abstractmethod
  def printInput(self):
    pass

  @abstractmethod
  def closeChar(self):
    pass

  def display(self):
    self.openChar()
    for i in range(0, 5):
      self.printInput() 
    self.closeChar()


class CharDisplay(AbstractDisplay):
  def __init__(self, ch):
    self.__ch = ch

  def openChar(self):
    print('<<', end = '')

  def printInput(self):
    print(self.__ch, end = '')

  def closeChar(self):
    print('>>')


class StringDisplay(AbstractDisplay):
  def __init__(self, string):
    self.__string = string
    self.__width = len(string.encode("UTF-8"))

  def openChar(self):
    self.__printLine()

  def printInput(self):
    print('|' + self.__string + '|')

  def closeChar(self):
    self.__printLine()

  def __printLine(self):
    print('+', end = '')
    for i in range(0, self.__width):
      print('-', end = '')
    print('+')


if __name__ == '__main__':
  d1 = CharDisplay('H')
  d2 = StringDisplay("Hello, World.")
  d3 = StringDisplay("こんにちは。")
  d1.display()
  d2.display()
  d3.display()








