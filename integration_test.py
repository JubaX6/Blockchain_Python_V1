import requests
import json


def test_mine_block():
    response = requests.get("http://localhost:5000/mine")
    assert response.status_code == 200
    data = response.json()
    assert data['message'] == "New Block Forged"
    assert 'index' in data
    assert 'transactions' in data
    assert 'proof' in data
    assert 'previous_hash' in data

def test_create_transaction():
    transaction_data = {
        "sender": "Juba",
        "recipient": "Ales",
        "amount": 5
    }
    response = requests.post("http://localhost:5000/transactions/new",
                             headers={"Content-Type": "application/json"},
                             data=json.dumps(transaction_data))
    assert response.status_code == 201
    data = response.json()
    assert 'message' in data
    assert 'Transaction will be added to Block' in data['message']

def test_get_chain():
    response = requests.get("http://localhost:5000/chain")
    assert response.status_code == 200
    data = response.json()
    assert 'chain' in data
    assert 'length' in data
    assert len(data['chain']) == data['length']

if __name__ == "__main__":
    test_mine_block()
    test_create_transaction()
    test_get_chain()
    print("All integration tests are successful.")