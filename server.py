from bottle import route, run, template
import calendar
import datetime
import aggregator


@route('/')
def index():
    return template('index.html', pages=aggregator.show_pages())


@route('/latest/')
def index():
    return template('latest.html', pages=aggregator.show_posts(), title='Latest posts')


@route('/<year>/<month>/<day>/')
def index(year, month, day):
    return template('latest.html', pages=aggregator.show_posts(year + '/' + month + '/' + day), title='Posts {}/{}/{}'.format(year, month, day))

if __name__ == "__main__":
    run(debug=True, reloader=True)