import praw
import time
import re

reddit = praw.Reddit('bot1')
user = reddit.redditor('the-hug-bot')

regexMatch = '.*need.*hug'

mentalHealthSubreddits = [
"mentalHealth",
"tifu",
"raisedbynarcissists",
"act",
"sat",
"applyingtocollege",
"teenagers",
"insaneparents",
"apstudents",
"offmychest"
]

'''
# Testing environment
mentalHealthSubreddits = [
"7iooibottesting"
]
'''


global commentList
commentList = []

def processComment(comment):
    global commentList
    commentID = comment.id
    if commentID not in commentList:
        bodyText = comment.body
        if re.search(regexMatch, bodyText, re.IGNORECASE):
            comment.reply("*Hug*")
            print("New comment posted.\n", flush=True)
            commentList.append(commentID)


while True:
    for sub in mentalHealthSubreddits:
        #print(commentList, flush=True)
        #print("Reading new subreddit...\n" + sub, flush=True)
        for comment in reddit.subreddit(sub).stream.comments(pause_after=0):
            time.sleep(0.01)
            if comment is None:
                break
            else:
                try:
                    processComment(comment)
                except:
                    print("Comment processing produced an error. Trying to wait to resolve problem.", flush=True) #New accounts are rate limited
                    time.sleep(60)
                    try:
                        processComment(comment)
                    except:
                        print("Failure! RATELIMIT is either too high or there is a fatal problem.", flush=True)
