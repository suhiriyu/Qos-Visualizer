import pandas as pd
from GetDictionary import data_dictionary
from Conversion import compare_lines_with_dict
from flask import Flask,render_template,request
app=Flask(__name__)
global config 
@app.route('/')
def welcome():
    return render_template('input.html')

@app.route('/templates/Output.HTML')
def abc():
    return render_template('output.html')

@app.route('/convert',methods=['POST','GET'])
def convert():
    config = request.form['inputconfig']
    print(config)
    choice1 = request.form['from-select']
    choice2 = request.form['to-select']
    if choice1 == "NONE" or choice2 == "NONE":
        return render_template('NoChoiceSelected.html')
    
    if choice1==choice2:
       return render_template('SameSeriesSelected.html')

    if choice1=="catalyst9k" and choice2=="nexus9k":
     if config=="":
         return render_template('NoInput.html')
     resultingdict=data_dictionary(choice1,choice2)
     result , faults = compare_lines_with_dict(config,resultingdict)
     return render_template('output.html',result=result,faults=faults)
    
    if choice1=="nexus9k" and choice2=="catalyst9k":
     if config=="":
         return render_template('NoInput.html')
     resultingdict=data_dictionary(choice1,choice2)
     result , faults = compare_lines_with_dict(config,resultingdict)
     return render_template('output.html',result=result,faults=faults)
     
    return render_template('ConversionNotPossible.html')
  
@app.route('/input')
def abcd():
    config=request.form['inputconfig']
    return render_template('Input.html',config=config)


if __name__=='__main__':
    app.run(debug=True)