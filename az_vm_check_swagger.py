from flask import Flask, request
import subprocess
from flask_cors import CORS
from flasgger import Swagger
app = Flask(__name__)
CORS(app) 
swagger = Swagger(app)


@app.route("/vm")
def hello():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: resourcegroup
        in: query
        type: string
        required: true
      - name: vmname
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
    vmname=request.args.get('vmname') 
    # cmd = (["az", "vm", "list", "--resource-group", str(resourcegroup) , "--show-details" ])
    cmd = (["az", "vm",  "show", "--name", str(vmname), "--resource-group", str(resourcegroup), "--show-details" ])
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
    cmd = (["az", "deployment", "operation", "group", "list", "--resource-group", str(resourcegroup), "--name", "vmnetworkinterface_template" ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out    
  
if __name__ == "__main__" :


 app.run(port=5017, host='0.0.0.0', debug=True)