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
#@date        2013-4-16

import theano.tensor as T
from theano import function

def add_scalars():
  x = T.dscalar('x')
  y = T.dscalar('y')
  z = x + y
  f = function([x, y], z)
  print(f(2, 4))
  print(f(5, 4))

def add_matrices():
  x = T.dmatrix('x')
  y = T.dmatrix('y')
  z = x + y
  f = function([x, y], z)
  print(f([[1, 2], [3, 4]], [[10, 20], [30, 40]]))
  
if __name__ == '__main__':
  add_scalars()
  add_matrices()