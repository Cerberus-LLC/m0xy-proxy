'''
    :: title           : __init__.py
    :: project         : m0xy
    :: notes           : This is my first opensource project, so please give me any suggestions on how to improve.

    Copyright (C) 2018 Cerberus, LLC

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import unittest
import m0xy


class M0xyTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.m0xy_client = m0xy.M0xyClient()
        super(M0xyTest, self).__init__(*args, **kwargs)

    def test_load_unchecked_proxies(self):
        self.assertIsInstance(self.m0xy_client.load_unchecked_proxies(),list)

    def test_calculate_time(self):
        self.m0xy_client.load_unchecked_proxies()
        self.assertTrue(self.m0xy_client.calculate_time(),int)