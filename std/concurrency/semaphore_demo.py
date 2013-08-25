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
import time

class Worker(threading.Thread):
  def __init__(self, sema, requests):
    threading.Thread.__init__(self)
    self.sema = sema
    self.requests = requests
    
  def run(self):
    for i in range(self.requests):
      self.sema.acquire()
      print('%s is processing request#%d' % (self.name, i))
      time.sleep(1)
      self.sema.release()
#      time.sleep(0.01)

def demo():
  sema = threading.Semaphore(2)
  workers = []
  for _ in range(4):
    worker = Worker(sema, 5)
    workers.append(worker)
  
  for worker in workers:
    worker.start()
  
  for worker in workers:
    worker.join()
  
if __name__ == '__main__':
  demo()