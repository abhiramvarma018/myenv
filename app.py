from flask import Flask
### WSGI APPLICATION
app=Flask(__name__)

@app.route('/')###DECORATOR ROUTE HOMEPAGE
def welcome():    ##binding function
    return'welcome to my web application hihi'

@app.route('/members')###add another url to open this route
def welcome1():
    return'welcome to my web application guyys'

if __name__=='__main__':
    app.run(debug=True) ##automatically updated the web application when we save