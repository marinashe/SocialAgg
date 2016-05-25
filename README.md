# SocialAgg
Aggregator of posts from facebook pages

add_page.py

>Gets a page by url or slug or page id. Adds to the DB basic info about the page (name, about, fans, picture)

show_pages.py

>Show pages in page list.

get_or_update_all_posts.py

>Get posts for all pages (latest 100 posts) and save them in DB.

show_posts.py

>Show recent 50 posts from all pages if no argument(date), else show posts from date X.

best_posts.py

>Show 3 posts with the most likes from all pages. 

index.html, latest.html, forday.html

>Templates for site.

static/css/aggregator.css

>css for site.

server.py

>Simple Bottle server.

aggregator.py

>Modul with functions for site.
