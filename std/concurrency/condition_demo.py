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
#@date        2013-1-24

import threading

count = 20
cond = threading.Condition()

class Producer(threading.Thread):
  def run(self):
    global count
    while True:
      if cond.acquire():
        if count > 10:
          cond.wait()
        else:
          count += 5
          print('%s produced 5, count=%d' % (self.getName(), count))
          cond.notify()
        cond.release()
          
class Comsumer(threading.Thread):
  def run(self):
    global count
    while True:
      if cond.acquire():
        if count <= 0:
          cond.wait()
        else:
          count -= 3
          print('%s comsumed 3, count=%d' % (self.getName(), count))
          cond.notify()
        cond.release()

def demo():
  for _ in range(2):
    p = Producer()
    p.start()
    
  for _ in range(5):
    c = Comsumer()
    c.start()
  
if __name__ == '__main__':
  demo()