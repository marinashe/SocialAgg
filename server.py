from bottle import route, run, template
import calendar
import datetime
import aggregator


@route('/')
def index():
    return aggregator.show_pages()


@route('/latest/')
def index():
    return aggregator.show_posts()


@route('/<year>/<month>/<day>/')
def index(year, month, day):
    return aggregator.show_posts(year +'/' +month + '/' + day)

if __name__ == "__main__":
    run(debug=True, reloader=True)