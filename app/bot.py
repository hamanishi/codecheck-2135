#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Bot():
  # Please write your code here.
  def __init__(self, data):
    self.command = data["command"]
    self.data = data["data"]

  def generate_hash(self):
    print(self.command)
    command_string = ""
    data_string = ""
    num_string = ""
    for char in self.command:
      command_string += str(ord(char))

    print(command_string)

    if len(command_string) >= 22:
      result = ""
      result = str(self.scientificNotation(float(command_string)))
      print(result)
      command_string = result.replace('e+','').replace('.',"")
      command_string = command_string[1:]
      print(command_string)

    for num in self.data:
      data_string += str(ord(num))

    if len(data_string) >= 22:
      result = ""
      result = str(self.scientificNotation(float(data_string)))
      print(result)
      data_string = result.replace('e+','').replace('.',"")
      data_string = data_string[1:]
      print(data_string)

    num_string = str(int(command_string, 10) + int(data_string, 10))

    self.hash = str(hex(int(num_string))).replace('0x','')
    print(self.hash)

  # Convert the number into scientific notation with 16 digits after "."
  # If power of e is greater than 20, get the number between "." and "e"
  # Else return the number itself
  def scientificNotation(self, num):
    data = "%.16e" % num
    result = data if (int(data.split("e+")[1]) > 20) else num
    return result
