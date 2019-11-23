# listenerr

An app realizing basiz DWT algorithm for planning and recognition

----

## Quick links
- [Features](#features)
- [Requirements](#requirements)
- [Project Setup](#project-setup)
- [Usage](#usage)
  - [Optional Arguments](#optional-arguments)
- [Contribute](#to-contribute)
- [Project Structure](#project-structure)
- [License](#license)

[↑](#listenerr)

----

## Features

[↑](#quick-links)

----

## Requirements

* [python](https://www.python.org/download/releases/3.0/) >= 3.2
* *(optional)* [pip](https://pypi.python.org/pypi/pip/)
* *(optional)* [venv](https://docs.python.org/3/library/venv.html)

[↑](#quick-links)

----

## Project Setup

* **Clone** the project
* Move into the **project dir**
* *(Optional)* Create a new **virtual environment**
* *(Optional)* Install project's **requirements**
* *(Optional)* View **documentation**
* *(Optional)* Run the **tests**
* *(Optional)* **Install** project's packages
* **Run** the project

**Step 1**: Clone the project:

    git clone https://github.com/nullhack/listenerr.git

**Step 2**: Move into project's path:

    cd listenerr

**Step 3**: *(Optional, but good practice)* Create a new virtual environment (ENV):
  
    python3 -m venv ENV
    source ENV/bin/activate

If you want to deactivate the virtual environment:

    deactivate

If you are new to virtual environments, please see the `Virtual Environment section` of Kenneth Reitz's [Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/).

**Step 4**: *(Optional)* Install project's requirements:

    pip3 install -r requirements.txt

**Step 5**: *(Optional)* View documentation:

    firefox docs/build/html/index.html

**Step 6**: *(Optional)* Run the tests:

    python3 -m doctest -v ./tests/*
    
**Step 7**: *(Optional)* Install project's packages:

    python3 setup.py install

**Step 11**: Run the project:

    python3 main.py

[↑](#quick-links)

----

## Usage: 

    main.py [-h] [-V]

### Optional arguments:

    -h, --help     show this help message and exit
    -V, --version  show program's version number and exit

[↑](#quick-links)

----

## To contribute

The general workflow that GitHub supports is:

* **Fork** this repo to your own account.
* **Clone** the repo to your machine.
* Check out a new **"topic branch"** and make changes.
* **Push** your topic branch to your fork.
* Use the diff viewer on GitHub to create a **pull request** via a discussion.
* Make any requested **changes**.
* The pull request is then **merged** and the "topic branch" is deleted from the upstream (target) repo.

The naming conventions for topic branches are: issue_ID, where the ID  is the ID # of a GitHub issue.

Use the official guides:

* https://help.github.com/articles/fork-a-repo/
* https://guides.github.com/activities/forking/

Or the reference [tutorial](https://code.tutsplus.com/tutorials/how-to-collaborate-on-github--net-34267) for this documentation.

Some commands that would complete the workflow above:

**Step 1**: Forking

In the top-right corner of the page, click **Fork Button**

**Step 2**: Cloning

Clone the repo using your own github login (YOUR_USERNAME):

    git clone git@github.com:YOUR_USERNAME/listenerr.git

**Step 3**: Adding the Upstream Remote

Change into the directory and then you can add the upstream remote:

    cd listenerr
    git remote add upstream git@github.com:nullhack/listenerr.git

To pull in changes from the source locally and merge them:

    git fetch upstream
    git merge upstream/master

**Step 4**: Checking Out a Topic Branch

Checkout a topic branch using the issue ID:

    git checkout -b issue_ID

**Step 5**: Committing

**Make your changes** and create a commit that tracks those changes.

    git commit -am "adding some specific change."

**Step 6**: Pushing

Push this topic branch to your own fork of the project.

    git push origin issue_ID

**Step 7**: Creating a Pull Request

Now you may create a pull request:

* Go to your fork of the repo
* Click on issue_ID at  "your recently pushed branches" 
* Choose "Compare and Pull Request"

Or:

* Select your branch from the dropdown
* click "Pull Request" or "Compare"

[↑](#quick-links)

----

## Project Structure

    listenerr
    ├── docs
    │   ├── make.bat
    │   ├── Makefile
    │   └── source
    │       ├── conf.py
    │       └── index.rst
    ├── LICENSE
    ├── main.py
    ├── MANIFEST.in
    ├── package_name
    │   ├── __init__.py
    │   └── metadata.py
    ├── README.md
    ├── requirements-dev.txt
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    └── tests
        └── test_metadata.txt

[↑](#quick-links)

----

## License

listenerr is released under GPL license.

Copyright (c) 2019 Bohdan Glushko

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Original license text can be found at the [LICENSE](LICENSE) file.

[↑](#quick-links)

----

