from flask import Flask, request
import subprocess
from flask_cors import CORS
from flasgger import Swagger
app = Flask(__name__)
CORS(app) 
swagger = Swagger(app)


@app.route("/publicip")
def hello():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: resourcegroup
        in: query
        type: string
        required: true
      - name: publicipname
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
    resourcegroup =request.args.get('resourcegroup') 
    publicipname =request.args.get('publicipname')  
    # cmd = (["az", "network", "public-ip", "list", "--resource-group", str(resourcegroup) ])
    cmd = (["az", "network", "public-ip", "show", "--name", str(publicipname), "--resource-group", str(resourcegroup) ]) 
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out

@app.route("/deployment")

def index():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: resourcegroup
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
    resourcegroup =request.args.get('resourcegroup')   
    cmd = (["az", "deployment", "operation", "group", "list", "--resource-group", str(resourcegroup), "--name", "publicip_template" ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out     
  
if __name__ == "__main__" :


 app.run(port=5015, host='0.0.0.0', debug=True)