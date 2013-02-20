#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2013 Binson Zhang.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
#@author     Binson Zhang <bin183cs@gmail.com>
#@date        2013-2-20

import csv

def read_comma():
  with open('comma.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
      print row

def read_tab():
  with open('tab.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
      print row

def write():
  o = []
  o.append(['Id', 'Name'])
  o.append([0, 'bin3'])
  o.append([1, 'cindy'])
  o.append([5, 'comma,tab end'])
  o.append([9, ['python', 'c++']])
  with open('write.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(o)

if __name__ == '__main__':
  read_comma()
  read_tab()
  write()
