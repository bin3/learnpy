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
#@date        2013-1-26

import pickle

class Person(object):
  def __init__(self, name = 'bin3', gender = 'male', age = 26):
    self.name = name
    self.gender = gender
    self.age = age
    
  def __repr__(self):
    return 'name=%s, gender=%s, age=%s' % (self.name, self.gender, self.age)

def dump(obj, path):
  print('dump path=%s' % path)
  print(obj)
  with open(path, 'wb') as f:
    pickle.dump(obj, f)

def load(path):
  print('load path=%s' % path)
  with open(path, 'rb') as f:
    obj = pickle.load(f)
    print(obj)
    
def dumps(obj):
  print('dumps obj=%s' % str(obj))
  s = pickle.dumps(obj)
  print(s)
  return s

def loads(s):
  print('loads s=%s' % s)
  obj = pickle.loads(s)
  return obj
    
def demo():
  DICT_PKL = 'dict.pkl'
  PERSON_PKL = 'pserson.pkl'
  d = {'name' : 'bin3', 'age': 26}
  p = Person()
  dump(d, DICT_PKL)
  dump(p, PERSON_PKL)
  load(DICT_PKL)
  load(PERSON_PKL)
  ds = dumps(d)
  loads(ds)

if __name__ == '__main__':
  demo()