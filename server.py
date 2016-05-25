from bottle import route, run, template, static_file
import calendar
import datetime
import aggregator


@route('/')
def index():
    return template('index.html', pages=aggregator.show_pages(),
                    day=aggregator.get_days_range()[1])


@route('/latest/')
def index():
    return template('latest.html', posts=aggregator.show_posts(),
                    title='Latest posts',
                    day=aggregator.get_days_range()[1]
                    )


@route('/<year>/<month>/<day>/')
def index(year, month, day):
    cur_day = year + '/' + month + '/' + day
    min_day, max_day = aggregator.get_days_range()
    return template('forday.html',
                    posts=aggregator.show_posts(cur_day),
                    title='Posts {}/{}/{}'.format(year, month, day),
                    min_day=min_day,
                    max_day=max_day,
                    day=cur_day
                    )


@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

if __name__ == "__main__":
    run(debug=True, reloader=True)