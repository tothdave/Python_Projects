import praw
import time

reddit = praw.Reddit(
    client_id="my client id",
    client_secret="my client secret",
    password="my password",
    user_agent="my user agent",
    username="my username"
)

dev_username = reddit.user.me()

## add a reply to a comment
def reply_comment():
    animal_comment = "I love dogs!"
    subreddit_funny_animals = reddit.subreddit("FunnyAnimals")

    for submission in subreddit_funny_animals.hot(limit=10):    
        for top_level_comment in submission.comments:
            if hasattr(top_level_comment, "body"):
                comment_lower = top_level_comment.body.lower()
                if " dog " in comment_lower:    
                    top_level_comment.reply(body=animal_comment)
                    time.sleep(660)

## add a reply to a post
def reply_post():
    technology_comment = "I just leave it here to find this post later."
    subreddit_technology = reddit.subreddit("technology")

    for submission in subreddit_technology.hot(limit=50):
        already_commented = False
        title_lower = submission.title.lower()
        if "microsoft" in title_lower:
            for comment in submission.comments:
                if hasattr(comment, 'author') and hasattr(comment.author, 'name'):
                    if comment.author.name == dev_username.name:
                        already_commented = True

            if not already_commented:
                print(f"Post title: {submission.title}\nCommenting something.\n")
                submission.reply(body=technology_comment)
                time.sleep(660)
            else:
                print(f"Post title: {submission.title}\nAlready made a comment on this post.")

reply_post()