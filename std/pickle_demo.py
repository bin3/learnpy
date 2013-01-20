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
#@date        2013-1-20

import pickle
import pprint

def dump():
  data1 = {'a': [1, 2.0, 3, 4+6j],
           'b': ('string', u'Unicode string'),
           'c': None}
  
  selfref_list = [1, 2, 3]
  selfref_list.append(selfref_list)
  
  output = open('data.pkl', 'wb')
  
  # Pickle dictionary using protocol 0.
  pickle.dump(data1, output)
  
  # Pickle the list using the highest protocol available.
  pickle.dump(selfref_list, output, -1)
  
  output.close()
  
def load():
  pkl_file = open('data.pkl', 'rb')

  data1 = pickle.load(pkl_file)
  pprint.pprint(data1)
  
  data2 = pickle.load(pkl_file)
  pprint.pprint(data2)
  
  pkl_file.close()

if __name__ == '__main__':
  dump()
  load()