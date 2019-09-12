"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from HW2 import app

if __name__ == '__main__':#保证当前程序所在的目录为根目录，而不是由其他文件引入了该模块
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080
    app.run(port=5555)
