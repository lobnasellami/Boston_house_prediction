import pickle 
from flask import Flask,render_template,request,jsonify
import numpy  as np 
import pandas as pd
app = Flask(__name__)
#loading the model 
model = pickle.load(open("regmodel.pkl",'rb'))
scaler=pickle.load(open("scalar.pkl",'rb'))
@app.route('/')
def home() :

    return render_template(r'home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data']
    print(f"**********{list(data.values())}****")
    print(np.array(list(data.values())).reshape(1,-1))
    new_input=scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output=model.predict(new_input)
    print(output)
    return(jsonify(output[0]))

if __name__ == "__main__":
    app.run(debug=True)
