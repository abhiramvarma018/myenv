### Building Url Dynamically
## variable rules and url building

from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'hii guyys'

@app.route('/success/<int:score>')##BUILDING DYNAMICALLY
def success(score):
    return 'the Person has passed and the marks is' + str(score)

@app.route('/fail/<int:score>')##BUILDING DYNAMICALLY
def fail(score):
    return 'the Person has failed and the marks is' + str(score)

##result checker
@app.route('/results/<int:marks>')##BUILDING DYNAMICALLY
def results(marks):
    result=""
    if marks<50:
        result="fail"
    else:
        result="success"
    return redirect(url_for(result,score=marks))

if __name__ == '__main__':
    app.run(debug=True)