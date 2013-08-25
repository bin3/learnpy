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

__author__ = 'Binson Zhang <bin183cs@gmail.com>'
__date__ = '2013-8-25'

def run(*args, **kwargs):
    print('------------')
    print('args: %s' % str(args))
    print('kwargs: %s' % str(kwargs))

if __name__ == '__main__':
    run(1, 2, 3, 4)
    run(a=1, b=2, c=3)
    run(1, 2, 3, a=1, b=2)
    run('a', 1, None, a=1, b='2')