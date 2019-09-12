"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

#Flask接受一个字符串作为参数，这个参数决定程序的根目录，
#以便于能找到相对于程序根目录的资源文件的位置，
#通常这种情况下都使用  __name__作为Flask参数。

import HW2.views
