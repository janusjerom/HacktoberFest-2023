# CONTRIBUTING

## GUIDELINES

After cloning this repo open the project folder in a _text-editor_(vs code is preferable). If you don't have vs-code in your machine, [install it](https://code.visualstudio.com/download)

## Pull Request Process

1. Fork the repository. 
2. Commit your changes to your fork. 
3. Submit a pull request.
4. Handle any feedback before the request is merged.
5. Accept our sincere Thank You!

### Folder Structure

```
├───Assets
└───Python

```
All the file you code should be created inside their respective programming language; Python folder only. Or else it will be treated as an "Invalid".

### Create a branch

Change to the repository directory on your computer (if you are not already there):

```
cd HacktoberFest-2023
```

Now create a branch using the `git checkout` command:

```
git checkout -b <your-new-branch-name>
```

For example:

```
git checkout -b add-john-doe
```

(The name of the branch does not need to have the word _add_ in it, but it's a reasonable thing to include because the purpose of this branch is to add your name to a list.)

### How to make necessary changes and commit those changes

Make changes based on what programming language code snippet you are adding.
For example : I want to write a program of a calculator in C++
PS: Make sure to add your Name and Programming name as the first two lines of the code snippet.

```python

# Python program for implementation of Selection
# Sort
import sys
A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):
	
	# Find the minimum element in remaining 
	# unsorted array
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j
			
	# Swap the found minimum element with 
	# the first element	 
	A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
	print("%d" %A[i],end=" , ") 

```

Please make sure your contribution is valuable and unique programming code snippets, so that we can make a beautiful blogpost out of it :)

## Now commit these changes

If you go to the project directory and execute the command git status, you'll see there are changes.
Add those changes to the branch you just created using the `git add` command:

```
git add .
```

Now commit those changes using the `git commit` command:

```
git commit -m "Added new <Your component name>"
```

## Push changes to github

Push your changes using the command `git push`:

```
git push origin <add-your-branch-name>
```

replacing `<add-your-branch-name>` with the name of the branch you created earlier.

## Submit your changes for review

If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.
Now submit the pull request.
Soon I'll be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

## Where to go from here?

Congrats!!🥳  
You just completed the standard fork -> clone -> edit -> pull request workflow that you'll encounter often as a contributor!

## PLEASE NOTE 

When contributing a major change to this repository, please first discuss the change you wish to make via an [email](contributing/ISSUES.md) or via
[Email](janusjerom2000@gmail.com). Minor issues can simply be addressed by sending by a pull request.

All [pull requests](contributing/PULL-REQUESTS.md) will require you to ensure the change is certified via the [Developer Certificate of Origin (DCO)](https://github.com/apps/dco/). The DCO is a lightweight way for contributors to certify that they wrote or otherwise have the right to submit the code they are contributing to the project.

Please note we have a [Code of Conduct](#code-of-conduct), please follow it in all your interactions with the project and its community.

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team on [Slack in the #droneaid channel](https://code-and-response.slack.com/join/shared_invite/enQtNzUzOTAzNDE3MTM4LWM4M2VlOTA3OWNjMjY0ZTI4MjQ2OTBjYjYwNmQ1NTdhYjZhODE5NjFkN2QyNmRkNDI5OTFlZmVjYTFhMmMwYmU). 

All complaints will be reviewed and investigated and will result in a response that is deemed necessary and appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident.Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4, available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/
All [pull requests](contributing/PULL-REQUESTS.md) will require you to ensure the change is certified via the [Developer Certificate of Origin (DCO)](https://github.com/apps/dco/). The DCO is a lightweight way for contributors to certify that they wrote or otherwise have the right to submit the code they are contributing to the project.
