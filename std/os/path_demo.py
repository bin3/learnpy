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
#@date        2013-8-25

import os

def run(path):
    print('------- path=%s' % path)
    print('normpath=%s' % os.path.normpath(path))
    print('dirname=%s' % os.path.dirname(path))
    print('basename=%s' % os.path.basename(path))
    
if __name__ == '__main__':
    path = '/usr/bin'
    run('/usr/bin')
    run('/usr/bin/')
    run('/usr/bin/../lib')