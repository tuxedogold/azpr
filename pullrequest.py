import os,subprocess,sys

def main():
    prompt()
    azlogin()
    bn = gitbranchname()
    print("branch name is "+bn)
    gitpush(bn)
    reviewer =  ''
    azpr(bn,reviewer)

def prompt():
    resp=input('''
    "Pre-PullRequest Checklist: 

    [ ] Commit all your changes?
    [ ] Pull origin master?
    [ ] Resolve any conflicts?

    Press enter or y to continue, anything else to quit"
 
    ''')
    if(resp != 'y' and resp != ''):
        sys.exit()
    
def azlogin():
    callProcess(["powershell","-Command","\"&Get-Content .key | az devops login\""]) #stdin is being weird so whatevs just use powershell

def gitbranchname():
    return callProcess(["git","branchname"]).strip("\n")

def gitpush(bn):
    print("running git push sending your branch with commits to azure")
    callProcess(["git","push", "--set-upstream","origin",bn])

def azpr(bn,reviewers):
    print("creating pull request named "+bn)
    callProcess(["az.cmd","repos","pr","create","--delete-source-branch","--squash","--open","--source-branch",bn,"--target-branch","master","--reviewers",reviewers,"--title",bn])

def callProcess(pargs):
    process = subprocess.Popen(pargs, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = process.communicate()[0]
    print(stdout)
    try:
        proc = subprocess.check_output(pargs, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        print("errors were found with \n {0} \n\n Exiting...".format(pargs))
        sys.exit()
    return stdout.decode('utf-8')

if __name__ == "__main__":
    main()
