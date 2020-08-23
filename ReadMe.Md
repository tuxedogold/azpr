# automated azure pull requests. 
Since azure devops does not give you a link after pushing changes to create a pull request out of the box, here is an automated command to push and generate a pull request.

# setup instructions

* open up a cmd prompt as administrator
* change directory to where you cloned this repo
* run `powershell &./setup.ps1`
* Go into your azure portal, click on settings in the top banner near your profile
* Click on Personel Acccess Token
* Create a PAT
* Save the value and cut/paste it into the empty .key file created by setup.ps1
* edit pullrequest.py and add reviewer IDs if you would like
* Finally, add this folder into your PATH environment variable for ease of use.

# usage:

Once you are ready to create a pull request, pull lastest from the master branch
then type

`azpr`


It will propmt you with a checklist to reivew. Press enter and it will push your latest changes and create a pull request titled as your branch name. It will also open that pull request so you can edit/add for further review
