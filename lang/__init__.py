"""
GiGi 101, Telegram Voice Chat Bot
Copyright (c) 2022-present babipanda <https://github.com/babipanda>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import json

# import os
# print("Current working directory: {0}".format(os.getcwd()))
# for f in os.listdir("/home/annu/Natan/Python/BOt/Test_1"):
	# print(f)

def load(lang):
    return json.load(open(f"./lang/en.json", "r"))
# print(load("update"))