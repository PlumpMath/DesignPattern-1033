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


class PrintBanner(Print):
  def __init__(self, string):
    self.__banner = Banner(string)

  def printWeak(self):
    self.__banner.showWithParen()

  def printStrong(self):
    self.__banner.showWithAster()


if __name__ == '__main__':
  p = PrintBanner('Hello')
  p.printWeak()
  p.printStrong()