import subprocess
from git import Git
import os
import sys


curriculum = ['js0', 'js1', 'js2', 'js3',
              'js7', 'js8', 'test']

# merges all the branches


def merge_all(lesson='js1'):
    g = Git()
    branches = map(lambda x: x.strip(), g.branch().split('\n'))

    challenges = list(filter(lambda x: lesson in x, branches))

    for p in challenges:
        subprocess.run(['git', 'merge', p, '-q'])

# create branches for the challenges in the lesson


def create_challenges(lesson='js1'):
    g = Git()
    problemsets = list(filter(lambda x: '.js' in x,
                              os.listdir(os.path.join(os.curdir, lesson))))

    for p in problemsets:
        subprocess.run(
            ['git', 'branch', '{}-{}'.format(lesson, p.replace('.js', ''))])


# main interface for the script
# to run the script, use python branches.py [FLAG] [LESSON]
# flags = '-merge' or 'new'
if __name__ == '__main__':
    if(len(sys.argv) == 3):

        if(sys.argv[1] == '-merge'):

            if sys.argv[2] == curriculum:
                merge_all(sys.argv[2])

            else:
                print('not a problem set')

        elif sys.argv[1] == '-new':
            if sys.argv[2] in curriculum:
                create_challenges(sys.argv[2])
