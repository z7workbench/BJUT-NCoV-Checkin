# BJUT-NCoV-Checkin
BJUT daily check-in script using Selenium, written in Python

**PLEASE NOTICE:** if you feel sick or have fever, **DO NOT USE THIS SCRIPT AND REPORT TO YOUR MENTOR OR TEACHER IMMEDIATELY!!** This repository just simplifies the check-in proceduce!!!

This script will use your **previous settings**, so please be careful.

I **am** working on it. Chrome and Firefox are available on Linux and Windows. Other drivers are not tested. I do not have a Mac, so I cannot test it on Mac. If you use macOS and meet some bugs, please commit a issue. 

## Why do you create this repository?
- This is my first time using Selenium;
- My phone cannot check in and get my location;
- I just want to simplify this procedure;
- Whoever built this report system is **brilliant**.

## Will you add this to your another app: [BJUTLoginApp](https://github.com/z7workbench/BJUTLoginApp)?
I am thinking about it! Recently I re-design that app, so it will take a while. 

## What do I need to run this?
You need:
- Google Chrome (or other chromium brower) or Firefox installed on your computer
- Driver for Chrome or Firefox
  - [chromedriver for Chromium and Google Chrome](https://chromedriver.chromium.org/downloads) or [Taobao mirror](http://npm.taobao.org/mirrors/chromedriver)
  - [geckodriver for Firefox](https://github.com/mozilla/geckodriver/releases)
- Python 3.6 and above

## How to use?
I suggest using ``virtualenv`` to create the environment by exectuing
```
// install virtualenv
pip install virtualenv
// if it does not working, try pypi mirrors or use:
python -m pip install virtualenv
virtualenv venv
```
Copy browser driver (chromedriver or geckodriver) to PATH or``.\venv\Script`` for Windows and ``./venv/bin`` for Linux.

If you are using Linux, please use ``chmod a+x <driver>`` to make the driver excutable.

Then activate
```
Windows:
.\venv\Script\activate
Linux:
source venv/bin/activate
```
Install packages
```
pip install selenium
```
### Daily check in
Run
```
python checkin.py -u <username> -p <password> -d <chrome|firefox|gecko>
```
If you don't want to type username and password every time, you can create a JSON file named ``userpass.json`` in the repository's root. In ``userpass.json``, you need to type
```
{
  "user": "xxx",
  "pass": "xxx"
}
```
Then run
```
python checkin.py -d <chrome|firefox|gecko>
```
All set!!

If your Chrome is in version 86, you can use ``chromedriver(.exe)`` in the ``driver`` folder. (x86-64)
