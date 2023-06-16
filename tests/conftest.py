import pytest
import random
import string
from api import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

@pytest.fixture()
def random_data():
    name = 'test_'+''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=8))
    email = 'test_'+''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=15))
    csv_file = 'Test_file'
    eval = "Perf=100"
    id = 1

    return {"name":name,"email":email,"csv_file":csv_file,"eval":eval,"id":id}
    

@pytest.fixture()
def filepath():
    return "./csv_data/real_estate.csv"
    


@pytest.fixture()
def target():
    return 'Y house price of unit area'