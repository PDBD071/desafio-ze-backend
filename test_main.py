from fastapi.testclient import TestClient
from app.main import app  # Certifique-se de importar a aplicação FastAPI corretamente

client = TestClient(app)

def test_create_partner():
    response = client.post("/partners/", json={
        "tradingName": "Adega da Cerveja - Pinheiros",
        "ownerName": "Zé da Silva",
        "document": "1432132123891/0001",
        "coverageArea": {
            "type": "MultiPolygon",
            "coordinates": [
                [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]
            ]
        },
        "address": {
            "type": "Point",
            "coordinates": [-46.57421, -21.785741]
        }
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Partner created successfully!"}
