from flask import Flask, render_template, jsonify

app =Flask(__name__)

JOBS=[{
    'id':1, 
    'title':'data analyst',
    'location':'Bengalaru',
    'salary' :'1000'

},
{
    'id':1, 
    'title':'data old',
    'location':'Bengalaru',
    'salary' :'1000'

},
{
    'id':1, 
    'title':'data newer',
    'location':'Bengalaru',
    'salary' :'1000'

}]

@app.route("/")
def hello_world():
    return render_template("index.html",jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)



if __name__=="__main__":
    app.run(debug=True)
