import time
import modules.ai as ai
from modules.config.configuration import config
from modules.utils import parse_have_want, print_new_post

def firehose(subreddit):
    for submission in subreddit.stream.submissions(skip_existing = not config.retrieve_older_posts):
        h, w = parse_have_want(submission.title)
        print_new_post(subreddit, submission.author, h, w, submission.url, submission.created_utc, submission.author_flair_text, submission.title)

def match(subreddit):
    post_stream = subreddit.stream.submissions(skip_existing = not config.retrieve_older_posts)
    
    author_has_lower = [s.lower() for s in config.author_has]
    author_wants_lower = [s.lower() for s in config.author_wants]
    
    for submission in post_stream:
        h, w = parse_have_want(submission.title)
        if any(s in h.lower() for s in author_has_lower) and any(s in w.lower() for s in author_wants_lower):
            print_new_post(subreddit, submission.author, h, w, submission.url, submission.created_utc, submission.author_flair_text, submission.title)

def match_llm(subreddit):
    try:
        openrouter = ai.OpenRouter(api_key=config.openrouter_api_key)
        
        for submission in subreddit.stream.submissions(skip_existing = not config.retrieve_older_posts):
            h, w = parse_have_want(submission.title)
            title_replaced: str = str(submission.title).replace("[H]", "[Have]").replace("[W]", "[Want]").strip()
            
            response = openrouter.llm(author_has_llm_query=config.author_has_llm_query, author_wants_llm_query=config.author_wants_llm_query, title=title_replaced)

            if openrouter.is_match(response):
                print_new_post(subreddit, submission.author, h, w, submission.url, submission.created_utc, submission.author_flair_text, submission.title)
            
            # sleep for 3 seconds to avoid API rate limiting, which would crash the script
            time.sleep(3)
            
    except Exception as e:
        raise Exception(f"{e.__dict__['body']['message']}")