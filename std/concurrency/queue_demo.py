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
#@date        2013-1-23

import threading
import Queue
import time

class Worker(threading.Thread):
  def __init__(self, queue):
    threading.Thread.__init__(self)
    self.queue = queue
    
  def run(self):
    while True:
      task = self.queue.get()
      print('%s is learning %s' % (self.getName(), task))
      self.queue.task_done()

def demo():
  tasks = ["Python", "Ruby", "Javascript", "PHP", "Java", "C++", "C", "Scala", 
           "Closure", "Haskell", "HTML5", "CSS", "Lisp"]
  queue = Queue.Queue()
  start = time.time()
  
  for _ in range(4):
    worker = Worker(queue)
    worker.setDaemon(True)
    worker.start()
  
  for task in tasks:
    queue.put(task)
    
  queue.join()
  print('Elapsed time %s' % (time.time() - start))

if __name__ == '__main__':
  demo()