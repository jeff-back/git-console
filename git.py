from time import sleep

def git(cmd):
    import os
    os.system(cmd)


commit = str(input('Nome do commit: '))
print('Git commit starting...')
sleep(2)

try:
    git('git init')
except:
    print('Repositório Existe')

git('git add -A')
git(f'git commit -m "{commit}"')
git('git status')