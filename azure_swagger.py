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
      - name: templatename
        in: query
        type: string
        required: true
      - name: resource_group_name
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


   templatename = request.args.get('templatename')
   resource_group_name =request.args.get('resource_group_name')
   os.system('/bin/bash --rcfile sh shell.sh '+ str(resource_group_name) + ' ' + str(templatename))
   return (
     '{\n'
     '   "status" : 200 \n'
     '}\n'
   )

if __name__=='__main__':   
    app.run(port=5007, host='0.0.0.0')