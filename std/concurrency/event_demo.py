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
#@date        2013-1-29

import threading
import time

def curname():
  return threading.current_thread().getName()

def wait(e):
  print('{}: waiting signal...'.format(curname()))
  e.wait()
  print('{}: event has been set'.format(curname()))
  
def signal(e, seconds):
  print('{}: sleeping for {} second...'.format(curname(), seconds))
  time.sleep(seconds)
  print('{}: set event'.format(curname()))
  e.set()
  
if __name__ == '__main__':
  e = threading.Event()
  e.clear()
  wait_thread = threading.Thread(target=wait, args=(e,))
  wait_thread.start()
  
  signal_thread = threading.Thread(target=signal, args=(e, 0.85))
  signal_thread.start()