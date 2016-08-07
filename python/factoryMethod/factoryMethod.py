#! /user/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class Product(metaclass = ABCMeta):
  @abstractmethod
  def use(self):
    pass


class Factory(metaclass = ABCMeta):
  def create(self, owner):
    p = self.createProduct(owner)
    self.registerProduct(p)
    return p

  @abstractmethod
  def createProduct(self, owner):
    pass

  @abstractmethod
  def registerProduct(self, product):
    pass


class IDCard(Product):
  def __init__(self, owner):
    print(owner + "のカードを作ります。")
    self.__owner = owner

  def use(self):
    print(self.__owner + "のカードを使います。")

  def getOwner(self):
    return self.__owner


class IDCardFactory(Factory):
  def __init__(self):
    self.__owners = []

  def createProduct(self, owner):
    return IDCard(owner)

  def registerProduct(self, product):
    self.__owners.append(product.getOwner())

  def getOwners(self):
    return self.__owners


if __name__ == '__main__':
  factory = IDCardFactory()
  card1 = factory.create("hoge")
  card2 = factory.create("piyo")
  card3 = factory.create("fuga")
  card1.use()
  card2.use()
  card3.use()
