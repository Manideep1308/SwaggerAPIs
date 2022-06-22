from flask import Flask, request
import boto3
from flask_cors import CORS
from flasgger import Swagger
app = Flask(__name__)
CORS(app) 
swagger = Swagger(app)

@app.route('/resource_check')
def func():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: stackname
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
    stackname =request.args.get('stackname')

    client = boto3.client('cloudformation')                     

    list = client.list_stack_resources(StackName = str(stackname)) 

    return list
    



app.run(port=5012, host="0.0.0.0",debug=True)     