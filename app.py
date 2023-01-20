from flask import Flask, render_template,request
import pickle


app=Flask(__name__)

with open('model.pkl','rb') as file:
    model=pickle.load(file)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict(): 
    
    mean_redius=int(request.form['mean_radius'])
    mean_texture=int(request.form['mean_texture'])
    mean_perimeter=int(request.form['mean_perimeter'])
    mean_area=int(request.form['mean_area'])
    mean_smoothness=int(request.form['mean_smoothness'])

    diagnosis=model.predict([[mean_redius,mean_texture,mean_perimeter,mean_area,mean_smoothness]])




    return render_template("index.html",diagnosis=diagnosis)

if __name__=='__main__':
    app.run(debug=True)

