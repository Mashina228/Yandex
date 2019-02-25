from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/image_sample')
def image():
    return '''<h1>Hello, Yandex!</h1><img src="{}" alt="здесь должна была быть картинка, 
    но не нашлась">'''.format(url_for('static', filename='img/Риана.jpeg'))


@app.route('/bootstrap_sample')
def bootstrap():
    return '''<div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
                <nav class="navbar navbar-light bg-light">
                  <span class="navbar-brand mb-0 h1">Navbar</span>
                </nav>
                <a class="btn btn-primary" href="#" role="button">Link</a>
                <button class="btn btn-primary" type="submit">Button</button>
                <input class="btn btn-primary" type="button" value="Input">
                <input class="btn btn-primary" type="submit" value="Submit">
                <input class="btn btn-primary" type="reset" value="Reset">
                <div class="carousel-inner">
                  <div class="carousel-item active">
                    <img class="d-block w-100" src="/static/img/Риана.jpeg" alt="First slide">
                  </div>
                  <div class="carousel-item">
                    <img class="d-block w-100" src="/static/img/second_.jpg" alt="Second slide">
                  </div>
                  <div class="carousel-item">
                    <img class="d-block w-100" src="https://thewallpaper.co/wp-content/uploads/2016/10/Amazing-beach-under-the-palms-wallpaper-wallpaper-desktop-images-hd-free-windows-wallpaper-samsung-iphone-mac-3840x2160.jpg" alt="Third slide">
                  </div>
                </div>
              </div>'''


@app.route('/text_in_alert/<text>')
def text_in_alert(text):
    return '''<div class="alert alert-primary" role="alert">
                {}
              </div>'''.format(text)


@app.route('/yandex_music')
def yandex_music():
    return '''<body>  
                <iframe frameborder="0" style="border:none;width:900px;height:600px;" width="900" height="600" src="https://music.yandex.ru/iframe/#album/5028955/">Слушайте <a href='https://music.yandex.ru/album/5028955'>Sick Boy</a> — <a href='https://music.yandex.ru/artist/2638699'>The Chainsmokers</a> на Яндекс.Музыке</iframe>
              </body>'''


@app.route('/list/<int:numm>')
def list(numm):
    a = '''<div class="alert alert-primary" role="alert">
           '''
    for i in range(1, numm + 1):
        a += str(i) + '''
             '''
    a += '''</div>'''
    return a


@app.route('/table/<int:n>/<int:m>')
def table(n, m):
    a = '''<table class="table">
             <tbody>'''
    for i in range(1, m + 1):
        a += '''<tr>'''
        for g in range(1, n + 1):
            a += '''<td>''' + str(i) + ';' + str(g) + '''</td>'''
        a += '''</tr>'''
    a += '''</tbody>
          </table>'''
    return a


@app.route('/youtube/<int:num>')
def youtube(num):
    if 5 >= num > 0:
        result = '''<body>
                    {}
                    {}
                    {}
                    {}
                    {}
                    <body>'''
        vse = [
            '''<iframe width="538" height="303" src="https://www.youtube.com/embed/dLACj0TpCRc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''',
            '''<iframe width="538" height="303" src="https://www.youtube.com/embed/QybvBUjCQpg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''',
            '''<iframe width="538" height="303" src="https://www.youtube.com/embed/YQvel9QFEOQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''',
            '''<iframe width="538" height="303" src="https://www.youtube.com/embed/d_pchAuH5lY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''',
            '''<iframe width="538" height="303" src="https://www.youtube.com/embed/WujKJpxaUHk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''']
        if num == 1:
            return result.format(vse[0], '', '', '', '')
        elif num == 2:
            return result.format(vse[0], vse[1], '', '', '')
        elif num == 3:
            return result.format(vse[0], vse[1], vse[2], '', '')
        elif num == 4:
            return result.format(vse[0], vse[1], vse[2], vse[3], '')
        else:
            return result.format(vse[0], vse[1], vse[2], vse[3], vse[4])
    return '''<div class="alert alert-primary" role="alert">
                {}
              </div>'''.format('Wrong Number')


@app.route('/image_puzzle/<int:num>')
def image_puzzle(num):
    if 16 >= num > 0:
        result = '''<table class="table">
                      <tbody>
                        <tr>
                          <td><img src="{}"</td>
                          <td><img src="{}"</td>
                          <td><img src="{}"</td>
                          <td><img src="{}"</td>
                        </tr>
                        <tr>
                          <td><img src="{}"</td>
                          <td><img src="{}"</td>
                          <td><img src="{}"</td>
                          <td><img src="{}"</td>
                        </tr>
                        <tr>
                          <td><img src="{}"</td>
                          <td><img src="{}"</td>
                          <td><img src="{}"</td>
                          <td><img src="{}"</td>
                        </tr>
                        <tr>
                          <td><img src="{}"</td>
                          <td><img src="{}"</td>
                          <td><img src="{}"</td>
                          <td><img src="{}"</td>
                        </tr>
                      </tbody>
                    </table>'''
        vse = ["img/Риана - копия (2).jpeg", "img/Риана - копия (3).jpeg", "img/Риана - копия (4).jpeg",
               "img/Риана - копия (4).jpeg",
               "img/Риана - копия (5).jpeg", "img/Риана - копия (6).jpeg", "img/Риана - копия (7).jpeg",
               "img/Риана - копия (8).jpeg",
               "img/Риана - копия (9).jpeg", "img/Риана - копия (12).jpeg", "img/Риана - копия (10).jpeg",
               "img/Риана - копия (11).jpeg", "img/Риана - копия (13).jpeg",
               "img/Риана - копия (14).jpeg",
               "img/Риана - копия (15).jpeg",
               "img/Риана - копия (16).jpeg"]
        zap = vse[:]
        zap[num - 1] = 'img/white.jpg'
        return result.format(url_for('static', filename=zap[0]), url_for('static', filename=zap[1]),
                             url_for('static', filename=zap[2]), url_for('static', filename=zap[3]),
                             url_for('static', filename=zap[4]), url_for('static', filename=zap[5]),
                             url_for('static', filename=zap[6]), url_for('static', filename=zap[7]),
                             url_for('static', filename=zap[8]), url_for('static', filename=zap[9]),
                             url_for('static', filename=zap[10]), url_for('static', filename=zap[11]),
                             url_for('static', filename=zap[12]), url_for('static', filename=zap[13]),
                             url_for('static', filename=zap[14]), url_for('static', filename=zap[15]))
    return '''<div class="alert alert-primary" role="alert">
                {}
              </div>'''.format('Wrong Number')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
