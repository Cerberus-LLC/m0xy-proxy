'''
    :: title           : __init__.py
    :: project         : m0xy
    :: notes           : Main m0xy client class

    Copyright (C) <year>  <name of author>

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

from multiprocessing.dummy import Pool as ThreadPool
import urllib.request as urllib2

class M0xyClient():

    def __init__(self):
        self.thread_pools = 300
        self.proxy_timeout = 10
        self.loaded_unchecked = False
        self.thread_pool = ThreadPool(self.thread_pools)
        return

    def load_unchecked_proxies(self):
        with open('m0xy/proxies.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        self.loaded_unchecked = content
        return content

    def check_ip(self, ip):
        try:
            proxy_handler = urllib2.ProxyHandler({'http': ip})
            opener = urllib2.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib2.install_opener(opener)
            req = urllib2.Request('http://www.icanhazip.com')
            urllib2.urlopen(req , None , self.proxy_timeout)
            return [ip, True]
        except:
            return [ip, False]

        return [ip, False]

    def check_loaded(self):
        working_proxies = list()
        if self.loaded_unchecked:
            results = self.thread_pool.map(self.check_ip, self.loaded_unchecked)
            for result in results:
                if result[1]:
                    working_proxies.append(result[0])

            self.loaded_unchecked = False
            self.active_proxies = active_proxies
            return active_proxies
        return

    def list_active_proxies

    def calculate_time(self):
        if self.loaded_unchecked:
            total_poxies = len(self.loaded_unchecked)
            thread_pools = self.thread_pools
            timeout = self.proxy_timeout
            total_pools = round(total_poxies / thread_pools)
            total_time = total_pools * timeout

            return total_time

        return