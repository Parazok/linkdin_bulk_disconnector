# linkdin_bulk_disconnector
disconnect your oldest connections easily

## disclamer

this software is made just for educational perposes so use it at your own risks.
there is a serious potential that your account get banned or permenantly blocked by linkedin.

THIS SOFTWARE IS PROVIDED BY DEVELOPERS AND CONTRIBUTORS “AS IS”.
THIS SOFTWARE IS MADE JUST FOR EDUCATIONAL PERPOSES AND HAS ABSOLUTLY NO WARRANTIES SO USE IT AT YOUR OWN RISKS.


## how to install

### clone the project
firsr clone project to your desiered location:

`git clone git@github.com:Parazok/linkdin_bulk_disconnector.git`

or if you prefere https:

`git clone https://github.com/Parazok/linkdin_bulk_disconnector.git`

### make virtual enviroment

make a virtual enviroment:

#### for linux:

`python3 -m venv venv`

#### for windows:

`python -m venv venv`

then make it active:

`source venv/bin/activate`

### install requeirments
use this command to install all required packages:

`pip install -r requirments.txt`

## how to use

##### before you use this software for the first time you need to do the folowing steps: (first time only or incase of wierd things happening)

1) first go to linkedin website using desktop computer and using a modern browser (chrome is recomended).

2) login to your account if you didn't already.

3) then press F12 on your keyboard (if you use chrome based browsers) or simply use right click and then inspect and go to network tab.

4) refresh the page.

5) right click on one off request and copy it as curl.

6) go to project directory and make a file named curl.txt

7) you are now all set to use this software

### run software on terminal

you can use this project by siply running the `main.py` file.

** make sure that virtual enviroment is activated **

`python main.py`








