import subprocess
import markdown
import random
import sys
import os

CHALLENGE_DIR = '{}/{}'.format(os.path.dirname(os.path.abspath(__file__)),'challenges')
challenges = []

def discoverChallenges(rootDir, difficulty = None):
    working_dir = rootDir
    if difficulty:
        working_dir = '{}/[{}]'.format(working_dir, difficulty)
    for (dirpath, dirnames, filenames) in os.walk(working_dir):
        challenges.extend(['{}/{}'.format(dirpath, f) for f in filenames])
        for dir in dirnames:
            discoverChallenges(dir)     

def convertToHTML(filePath):    
    outfile = '{}.html'.format(challenge[:-3]).replace('\\', '/')    
    challenge_text = ''    
    with open(challenge) as c:            
        challenge_text = ''.join(c.readlines())
    html = markdown.markdown(challenge_text)    
    with open(outfile, 'w+') as o:
        o.write(html)    
    print(outfile)

def main():
    difficulty = raw_input('Easy, Intermediate, or Hard: ')
    discoverChallenges(CHALLENGE_DIR, difficulty)    
    challenge = random.choice(challenges)
    print(challenge)
        

if __name__ == '__main__':
    sys.exit(int(main() or 0))