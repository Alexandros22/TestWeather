This is an application that shows the weather in some cities. Created from tutorial pages like:

https://www.freecodecamp.org/news/how-to-build-a-web-app-using-pythons-flask-and-google-app-engine-52b1bb82b221/

and the purpose is to learn and develop apps with Flask.

To run the app we need to have install:

Python 2.7+ 
pip
the modules from requirements.txt file

There are many pages in web that say how to install Python and Pip.
Supose that the above are installed then we can install the modules from requirements.txt file
using pip with this command in linux terminal or windows PowerShell:

>  pip install -r requirements.txt


If we are not facing any issue then we can see our app in a web broswer at:

http://localhost:5000/


If you want to use the Dockerfile and build a docker image then don not forget to change the flask's IP from 127.0.0.1 to 0.0.0.0 (all). To do that, open main.py and change the last line, app.run(debug=True), with app.run(host='0.0.0.0').
