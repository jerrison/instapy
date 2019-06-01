# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import schedule
import time

# login credentials
insta_username = "jerrisonli"
insta_password = "Comida1@"


# path to your workspace
set_workspace(path=None)

comments = [
    "Nice shot! @{}",
    "I love your profile! @{}",
    "Your feed is an inspiration :thumbsup:",
    "Just incredible :open_mouth:",
    "What camera did you use @{}?",
    "Love your posts @{}",
    "Looks awesome @{}",
    "Getting inspired by you @{}",
    ":raised_hands: Yes!",
    "I can feel your passion @{} :muscle:",
]

def job():
    # get an InstaPy session!
    # set headless_browser=True to run InstaPy in the background
    session = InstaPy(
        username=insta_username, password=insta_password, headless_browser=False
    )

    with smart_run(session):
        """ Activity flow """
        # general settings
        session.set_dont_include(["friend1", "friend2", "friend3"])

        # activity
        session.set_user_interact(amount=3, randomize=True, percentage=100, media="Photo")
        session.set_relationship_bounds(
            enabled=True,
            potency_ratio=None,
            delimit_by_numbers=True,
            max_followers=3000,
            max_following=900,
            min_followers=50,
            min_following=50,
        )

        session.set_do_follow(enabled=True, percentage=100)
        session.set_do_comment(enabled=True, percentage=100)
        session.set_comments(comments)
        session.unfollow_users(
            amount=60,
            InstapyFollowed=(True, "all"),
            style="FIFO",
            unfollow_after=90 * 60 * 60,
            sleep_delay=501,
        )

        session.like_by_tags(
            ["photo", "photography", "nature", "natgeo", "world"], amount=25, interact=True
        )

        session.unfollow_users(
            amount=60,
            InstapyFollowed=(True, "all"),
            style="FIFO",
            unfollow_after=90 * 60 * 60,
            sleep_delay=501,
        )

        # Joining Engagement Pods
        session.join_pods()

schedule.every().day.at("08:20").do(job)
schedule.every().day.at("16:22").do(job)

while True:
  schedule.run_pending()
  time.sleep(10)