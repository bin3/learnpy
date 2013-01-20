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

import logging.config

FORMAT = '[%(asctime)-15s %(threadName)s %(filename)s/%(funcName)s:%(lineno)d %(levelname)s] %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logging.config.fileConfig('logging.conf')

logger = logging.getLogger(__name__)

def simple():
  logging.debug('debug message')
  logging.info('info message')
  logging.warn('warn message')

def logging_to_file():
  logging.basicConfig(filename='logging.log',level=logging.DEBUG)
  logging.debug('This message should go to the log file')
  logging.info('So should this')
  logging.warning('And this, too')
  
def use_logger():
  logger.debug('debug message')
  logger.info('info message')
  logger.warn('warn message')
  logger.error('error message')
  logger.critical('critical message')

if __name__ == '__main__':
  simple()
  logging_to_file()
  use_logger()