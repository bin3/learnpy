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

# Echo server program
import socket

def run():
  HOST = ''                 # Symbolic name meaning all available interfaces
  PORT = 50007              # Arbitrary non-privileged port
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((HOST, PORT))
  s.listen(1)
  conn, addr = s.accept()
  print 'Connected by', addr
  while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
  conn.close()

if __name__ == '__main__':
  print('---echo_server---')
  run()