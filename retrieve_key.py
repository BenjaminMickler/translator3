__author__ = "Benjamin Mickler"
__copyright__ = "Copyright 2022, Benjamin Mickler"
__credits__ = ["Benjamin Mickler"]
__license__ = "GPLv3 or later"
__version__ = "01102022"
__maintainer__ = "Benjamin Mickler"
__email__ = "ben@benmickler.com"

"""
This file is part of translator3.

translator3 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

translator3 is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
translator3. If not, see <https://www.gnu.org/licenses/>.
"""

import base64
import rsa
pkey = rsa.PrivateKey.load_pkcs1(open('private.pem').read())
key = input("Key: ")
key = base64.b64decode(key.encode())
key = rsa.decrypt(key, pkey)
print(key.decode())
