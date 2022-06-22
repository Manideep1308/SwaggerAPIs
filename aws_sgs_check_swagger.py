from flask import Flask, request
import boto3
from flask_cors import CORS
from flasgger import Swagger
app = Flask(__name__)
CORS(app) 
swagger = Swagger(app)

@app.route('/sg_check')
def func():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: securitygroupname
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
    securitygroupname =request.args.get('securitygroupname')
   
    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups(
           Filters=[
      
          {
            'Name': 'group-name',
            'Values': [
                str(securitygroupname)
            
            ]
        }
        
    ]
)
    return (response)
    



app.run(port=5010, host="0.0.0.0",debug=True)    