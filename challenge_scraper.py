import os
import sys
import praw, pprint, re

CHALLENGES_DIR = os.curdir + '/challenges/'
USER_AGENT = 'Daily Programmer Challenge Scraper by Matt'
DIFFICULTY_PATTERN = r'\[(Easy|Intermediate|Hard)\]'
FILE_EXTENSION = '.md'
RETRIEVAL_ERROR = 'THERE WAS AN ERROR RETRIEVING THE CHALLENGE...'

def main():    
    r = praw.Reddit(user_agent=USER_AGENT)
    already_done = []
    sub = r.get_subreddit('dailyprogrammer')    
    for submission in sorted(sub.get_top_from_all(limit=1000), key=lambda p: p.title):        
        if submission.id not in already_done and containsDifficulty(submission.title):
            full_path = buildFullPath(submission)
            writeToFile(submission, full_path)
            already_done.append(submission.id)

def buildFullPath(submission):
    difficulty_dir = getDifficulty(submission.title)
    difficulty_path = CHALLENGES_DIR + difficulty_dir + '/'
    ensureDir(difficulty_path)
    file_name = stripIllegalPathCharacters(submission.title) + FILE_EXTENSION            
    return difficulty_path + '/' + file_name 

def writeToFile(submission, full_path):
    with open(full_path, 'wb') as f:
        text = ''
        try:
            text = submission.selftext.encode('ascii')                
        except UnicodeError:
            text = submission.selftext.encode('utf8')                
        except:                
            text = 'THERE WAS AN ERROR RETRIEVING THE CHALLENGE...'.join(sys.exc_info())
            print(text)
        finally:
            f.write(text)
            f.flush()                

def stripIllegalPathCharacters(s):
    return s.replace('/','-').replace('?','').replace(':', '-')

def containsDifficulty(s):
    return re.search(DIFFICULTY_PATTERN, s) != None

def getDifficulty(s):
    match =  re.search(DIFFICULTY_PATTERN, s)
    try:    
        if match:
            return match.group(0)
    except:
        return '[Unknown]'

def ensureDir(path):
    if not os.path.exists(path):
        os.makedirs(path)

if __name__ == '__main__':
    sys.exit(int(main() or 0))