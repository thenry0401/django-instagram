from config.celery import app


@app.task
def update_post_like_count(post):
    post.calc_like_count()
    return post.like_count