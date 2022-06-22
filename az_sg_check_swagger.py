from flask import Flask, request
import subprocess
from flask_cors import CORS
from flasgger import Swagger
app = Flask(__name__)
CORS(app) 
swagger = Swagger(app)


@app.route("/nsg")
def hello():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: resourcegroup
        in: query
        type: string
        required: true
      - name: nsgname
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
    nsgname =request.args.get('nsgname')   
    # cmd = (["az", "network", "nsg", "list", "--resource-group", str(resourcegroup) ])
    cmd = (["az", "network", "nsg", "show", "--name", str(nsgname), "--resource-group", str(resourcegroup) ])
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
    cmd = (["az", "deployment", "operation", "group", "list", "--resource-group", str(resourcegroup), "--name", "secgroup_template" ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out    
  
if __name__ == "__main__" :


 app.run(port=5014, host='0.0.0.0', debug=True)