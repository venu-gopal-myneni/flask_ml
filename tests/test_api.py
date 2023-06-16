
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to ML App" in response.data

def test_tenants(client):
    response = client.get("/tenants")
    assert response.status_code == 200


def test_metadata(client):
    response = client.get("/metadata")
    assert response.status_code == 200

def test_post_tenant(client,random_data):
    name = random_data["name"]
    email = random_data["email"]
    response = client.post("/add_tenant", json=dict(tenantname= name,email=email ))
    assert response.status_code == 200

def test_post_metadata(client,random_data):
    filename = random_data["csv_file"]
    eval = random_data["eval"]
    tenant_id=random_data["id"]
    response = client.post("/add_metadata", json=dict(filename= filename,eval=eval,tenant_id=tenant_id ))
    assert response.status_code == 200