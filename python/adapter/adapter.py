#! /user/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class Banner():
  def __init__(self, string):
    self.__string = string

  def showWithParen(self):
    print('(' + self.__string + ')')

  def showWithAster(self):
    print('*' + self.__string + '*')


class Print(metaclass = ABCMeta):
  @abstractmethod
  def printWeak(self):
    pass

  @abstractmethod
  def printStrong(self):
    pass


class PrintBanner(Banner, Print):
  def __init__(self, string):
    super().__init__(string)

  def printWeak(self):
    super().showWithParen()

  def printStrong(self):
    super().showWithAster()


if __name__ == '__main__':
  p = PrintBanner('Hello')
  p.printWeak()
  p.printStrong()