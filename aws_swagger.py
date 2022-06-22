from flask import Flask, request
import os
from flask_cors import CORS
from flasgger import Swagger
app = Flask(__name__)
CORS(app) 
swagger = Swagger(app)

@app.route('/name', methods=['POST'])
def method():
   """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: stacknames
        in: query
        type: string
        required: true
      
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """ 
   
   

   stacknames = request.args.get('stacknames')
   os.system('/bin/bash --rcfile sh bero.sh '+ str(stacknames))
   return (
     '{\n'
     '   "status" : 200 \n'
     '}\n'
   )


@app.route('/append', methods=['POST'])
def index():
  """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: classname
        in: query
        type: string
        required: true
      - name: stackname
        in: query
        type: string
        required: true        
      - name: path
        in: query
        type: string
        required: true    
      - name: accountnumber
        in: query
        type: string
        required: true
      - name: region
        in: query
        type: string
        required: true       
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """  
  classname = request.args.get('classname')
  stackname = request.args.get('stackname')
  path = request.args.get('path')
  accountnumber =request.args.get('accountnumber')
  region = request.args.get('region')  

  with open('/app/app.py','r') as f:
    contents = f.readlines()
  contents.insert(48, str(classname)+ "(app, '" + str(stackname)+ "', env=cdk.Environment(account= '" + str(accountnumber) +"', region='" + str(region)+ "'))\n")
  contents.insert(6, "from " + str(path) + " import " + str(classname) +"\n")
  with open('/app/app.py','w') as f:
    contents = "".join(contents)
    f.write(contents)

    return (
    '{\n'
     '   "status" : 200 \n'
     '}\n'
    )     

if __name__=='__main__':   
    app.run(port=5006, host='0.0.0.0')