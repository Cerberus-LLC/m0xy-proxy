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

import m0xy

m0xy_client = m0xy.M0xyClient()

print("\nTotal Proxies to Check: %s" % (len(m0xy_client.load_unchecked_proxies),))

print("\nApprox Time Remaining: %s seconds" % (m0xy_client.calculate_time(),))

print("\nTotal Working Proxies: %s \n\n" % (len(m0xy_client.check_loaded()),))

print("\nGood Proxies: \n\n%s" % (m0xy_client.list_active_proxies(),))
