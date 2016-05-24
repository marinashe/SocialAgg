from bottle import route, run, template
import calendar
import datetime
import aggregator


@route('/')
def index():
    return template('index.html', pages=aggregator.show_pages(),
                    today=(datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y/%m/%d'))


@route('/latest/')
def index():
    return template('latest.html', pages=aggregator.show_posts(),
                    title='Latest posts',
                    today=(datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y/%m/%d')
                    )


@route('/<year>/<month>/<day>/')
def index(year, month, day):
    return template('forday.html',
                    pages=aggregator.show_posts(year + '/' + month + '/' + day),
                    title='Posts {}/{}/{}'.format(year, month, day),
                    today=datetime.datetime.today().strftime('%Y/%m/%d')
                    )

if __name__ == "__main__":
    run(debug=True, reloader=True)