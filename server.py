from bottle import route, run, template, static_file
import calendar
import datetime
import aggregator


@route('/')
def index():
    return template('index.html', pages=aggregator.show_pages(),
                    today=(datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y/%m/%d'))


@route('/latest/')
def index():
    return template('latest.html', posts=aggregator.show_posts(),
                    title='Latest posts',
                    today=(datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y/%m/%d')
                    )


@route('/<year>/<month>/<day>/')
def index(year, month, day):
    return template('forday.html',
                    posts=aggregator.show_posts(year + '/' + month + '/' + day),
                    title='Posts {}/{}/{}'.format(year, month, day),
                    today=(datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y/%m/%d')
                    )


@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

if __name__ == "__main__":
    run(debug=True, reloader=True)