#
# @author DavidAwad
#
#

import git
import os
import subprocess
import click
import requests
import secrets

key_global = "TODO"
user_global = secrets.g_user
repo_global = "insightweets"

def grab_repo(uname, repo):
    # clone repo into local directory.
    git.Repo.clone_from('https://github.com/'+uname+'/'+repo, 'local/')


# recursively traverse through a directory
def process_repo():
    print 'cleaning out the .git folder'
    proc = subprocess.Popen('rm -rf local/.git', stdout=subprocess.PIPE, shell=True)
    proc.communicate() # pipe output to STDOUT
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk("local/"):
        # path = root.split('/')
        # print root - 'local/'
        # print dirs - [ folder1/ , folder2/ ]
        # print files
        # go through every line of every file in the given repo
        for inode in files:
            # print 'processing : local/'+inode
            process_file('local/'+inode)
        for dirent in dirs:
            iter_direc('local/'+dirent)

# recursively traverse the directory tree to find files and maintain paths
# note: this isn't an optimal way to do this as it attempts all possibilities
def iter_direc(dirent):
    for root, dirs, files in os.walk(dirent):
        # print os.path.basename(root)
        for inode in files:
            # print 'processing : '+dirent+'/'+inode
            process_file(dirent+'/'+inode)
        for curr_dirent in dirs:
            # print dirent+'/'+curr_dirent
            iter_direc(dirent+'/'+curr_dirent)

def process_file(arg_file):
    if not os.path.isfile(arg_file):
        return

    print 'opening ' + arg_file
    ## open the local folder and access arg_file
    log = open(arg_file, 'r')
    file_lines = log.readlines()
    log.close()

    fileEntry = [ ]
    for line in file_lines: # check for custom global in line
        if key_global in line:
            fileEntry.append(line)
    print 'entry is' + str(fileEntry) + '\n'


def create_issue(title, desc):
    # create an issue on the given repo.
    print "https://api.github.com/repos/"+user_global+'/'+repo_global+"/issues/ -u "+secrets.g_user+':'+secrets.g_pass

    r = requests.post(
            "https://api.github.com/repos/"+user_global+'/'+repo_global+"/issues/ -u "+secrets.g_user+':'+secrets.g_pass ,
              title = title
              # body = desc
        )
    print(r.status_code, r.reason)
    # 201 means issue was Created
    if r.status_code != 201 :
        print "ISSUE CREATION FAILED??"
        print r
    else:
        print "Created Issue Successfully!"

# TODO add support for filetypes like js or py, make a big list and run through

@click.command()
@click.option('-key', default='TODO', help='Trigger Keyword.')
@click.option('-user', prompt='GitHub Username?', help='The GitHub Username')
@click.option('-repo', prompt='GitHub Repository', help='The name of the Repository')
def start(key, user, repo):
    """Small CLI to lint your code for keywords and create GitHub issues.
    You can specift a -key TODO or -key ??? and create issues for the ocurrences
    of any string."""
    print 'downloading http://github.com/'+user+'/'+repo
    user_global = user
    repo_global = repo
    if key != 'TODO':
        key_global = key
        print 'Linting for special keyword ' + key_global

    grab_repo(user,repo)
    process_repo()


#if __name__ == '__main__':
#    start()

create_issue('yolo' , 'yolo')

''' TODO
import inspect

print inspect.__file__
print inspect.currentframe().f_lineno
'''
