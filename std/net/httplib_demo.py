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
#@date        2013-4-24

import httplib
import urllib

def get():
  conn = httplib.HTTPConnection('www.baidu.com')
  #params = urllib.urlencode({'wd': '天天向上'})
  conn.request('GET', '/s?wd=天天向上')
  r = conn.getresponse()
  print r.status, r.reason
  data = r.read()
  print data
  with open('baidu.html', 'w') as outf:
    outf.write(data)

if __name__ == '__main__':
  get()