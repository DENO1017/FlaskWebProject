"""
Routes and views for the flask application.
"""
import os
from datetime import datetime
from flask import render_template
from HW2 import app
#创建路由映射 
from HW2 import music


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'music.html',
        title='Home Page',
        year=datetime.now().year,
    )

#以上代码创建了一个由根目录'/home'到视图函数home()的映射
#即在浏览器中输入/home作为URL时，视图函数将返回值：'index.html'传递给浏览器。
#上面视图函数返回了一个静态的字符串“hello  world”，
#有时候我们不仅需要返回静态字符串，还需要根据用户在Url中的不同输入，
#来动态的进行返回不同的字符串，如根据用户输入的名字，
#显示不同的欢迎信息，这时就需要利用路由中的站位符：

@app.route('/dislike')
def dislike():
    """Renders the about page."""
    files = []
    images = []
    dislikes = []
    text = []
    PATH = 'E:\DAM\FlaskWebProject1\FlaskWebProject1\HW2\static\playlists\dislike\content'
    for file in music.get_filename(PATH,'.txt'):
        files.append(file)
        file_object = open(PATH+'\\'+file+ '.txt' )
        lines=file_object.readlines()
        m = music.music(file,lines[0],lines[1],lines[2],lines[3],'dislike/')
        dislikes.append(m)


    return render_template(
        'music.html',
        title='Dislikes',
        year=datetime.now().year,
        musics=dislikes
    )

@app.route('/favorite')
def favorite():
    """Renders the about page."""
    files = []
    images = []
    favorites = []
    text = []
    PATH = 'E:\DAM\FlaskWebProject1\FlaskWebProject1\HW2\static\playlists\\favorite\content'
    for file in music.get_filename(PATH,'.txt'):
        files.append(file)
        file_object = open(PATH+'\\'+file+ '.txt' )
        lines=file_object.readlines()
        m = music.music(file,lines[0],lines[1],lines[2],lines[3],'favorite/')
        favorites.append(m)


    return render_template(
        'music.html',
        title='Favorite',
        year=datetime.now().year,
        musics=favorites
    )

@app.route('/playlist')
def playlist():
    """Renders the about page."""
    playlists=music.get_playlist_ol()
    return render_template(
        'playlist.html',
        title='Hit Playlist',
        year=datetime.now().year,
        playlists=playlists
    )

@app.route('/_playlist_/<id>')
def _playlist_(id):
    """Renders the about page."""
    title = music.get_music_ol(id)
    return render_template(
        'list_music.html',
        title=title,
        year=datetime.now().year,
        list_id=id
    )

