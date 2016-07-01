import os
import sys
import praw, pprint, re

challenges_dir = os.curdir + '/challenges/'

def main():    
    

    r = praw.Reddit(user_agent='Daily Programmer Challenge Scraper by Matt')

    already_done = []
    sub = r.get_subreddit('dailyprogrammer')
    
    for submission in sorted(sub.get_top_from_all(limit=1000), key=lambda p: p.title):        
        if submission.id not in already_done and containsDifficulty(submission.title):
            difficulty_dir = getDifficulty(submission.title)
            difficulty_path = challenges_dir + difficulty_dir + '/'
            ensureDir(difficulty_path)

            file_name = stripSpecials(submission.title) + '.md'            
            full_path = difficulty_path + '/' + file_name 
            with open(full_path, 'wb') as f:
                text = ''
                try:
                    text = submission.selftext.encode('ascii')                
                except UnicodeError:
                    text = submission.selftext.encode('utf8')                
                except:                
                    print('error with file...', sys.exc_info()[1], sys.exc_info()[2])
                finally:
                    f.write(text)
                    f.flush()                
            already_done.append(submission.id)

def stripSpecials(s):
    return s.replace('/','-').replace('?','').replace(':', '-')

def containsDifficulty(s):
    return re.search('\[Easy|Intermediate|Hard\]', s) != None

def getDifficulty(s):
    match =  re.search('\[(Easy|Intermediate|Hard)\]', s)
    if match:
        return match.group(1)
    return '[Unknown]'

def ensureDir(path):
    if not os.path.exists(path):
        os.makedirs(path)

if __name__ == '__main__':
    sys.exit(int(main() or 0))