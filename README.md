# flask_ml
A simple app to train, evaluate and store ML models
# Usage
## Setting up and running Flask server
* Install Python3.11 on your local system
* Clone the repo to your local system
* Open a 'cmd terminal' and navigate to FLASK_ML directory on the local repo
* Create a virtual environment "pip -m venv venv"
* Activate the virtual environment "venv\Scripts\activate"
* Install requirements "pip install -r requirements.txt"
* Run "python run_app.py" to start flask app server
* "http://127.0.0.1:5000/tenants" list of existing tenants
* "http://127.0.0.1:5000/metadata"  list of existing metadata

## Client
* Open a second terminal and navigate to FLASK_ML directory on the local repo
* Activate the virtual environment "venv\Scripts\activate"
* Add your configuration settings to .env file
* Run "python main_client.py"
