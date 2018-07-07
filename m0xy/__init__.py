"""
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
"""

import multiprocessing.dummy
import typing
import urllib.error
import urllib.request


class M0xyClient:

    def __init__(self):
        self.thread_pools = 300
        self.proxy_timeout = 10
        self.loaded_unchecked = False
        self.thread_pool = multiprocessing.dummy.Pool(self.thread_pools)
        self.active_proxies = False

        return

    def load_unchecked_proxies(self, return_list = False):
        try:
            with open('proxies.txt') as f:
                content: typing.List[str] = f.readlines()
        except FileNotFoundError:
            raise ValueError('proxies.txt not found.')

        content = [x.strip() for x in content]

        if content:
            self.loaded_unchecked = content
            if return_list:
                return content
        else:
            raise ValueError('proxies.txt is empty.')

    def check_ip(self, ip):
        try:
            proxy_handler: urllib.request.ProxyHandler = urllib.request.ProxyHandler({'http': ip})
            opener = urllib.request.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            req = urllib.request.Request('http://www.icanhazip.com')
            urllib.request.urlopen(req, None, self.proxy_timeout)
            return [ip, True]
        except urllib.error.URLError:
            return [ip, False]

    def check_loaded(self):
        working_proxies = list()
        if self.loaded_unchecked:
            results = self.thread_pool.map(self.check_ip, self.loaded_unchecked)
            for result in results:
                if result[1]:
                    working_proxies.append(result[0])

            self.loaded_unchecked = False
            self.active_proxies = working_proxies

            return working_proxies
        return

    def list_active_proxies(self):
        if self.active_proxies:
            return self.active_proxies
        return

    # noinspection PyTypeChecker
    def calculate_time(self):
        if self.loaded_unchecked:
            total_poxies = len(self.loaded_unchecked)
            thread_pools = self.thread_pools
            timeout = self.proxy_timeout
            total_pools = round(total_poxies / thread_pools)
            total_time = total_pools * timeout

            if not total_time:
                total_time = self.proxy_timeout

            return total_time

        return
