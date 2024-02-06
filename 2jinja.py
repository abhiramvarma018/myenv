### Integrate HTML With Flask
### HTTP verb GET And POST

##Jinja2 template
'''
{%...%}conditions,for loop  statements
{{   }}expressions to print output
{#...#}this is for comments
'''
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')
 
@app.route('/success/<int:score>')##BUILDING DYNAMICALLY
def success(score):
    res=""
    if score>35:
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score,'res':res}
    return render_template('result.html',result=exp)

@app.route('/fail/<int:score>')##BUILDING DYNAMICALLY
def fail(score):
    return 'the Person has failed and the average mark is ' + str(score)

##result checker
@app.route('/results/<int:marks>')##BUILDING DYNAMICALLY
def results(marks):
    result=""
    if marks<35:
        result="fail"
    else:
        result="success"
    return redirect(url_for(result,score=marks)) 

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=''

    return redirect(url_for('success',score=total_score))

if __name__ == '__main__':
    app.run(debug=True)