from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

test_json = {
    'bf':'+++++++++[>++++++++>+++++++++++>+++>+<<<<-]>.>++.+++++++..+++.>+++++.<<+++++++++++++++.>.+++.------.--------.>+.>+.'
}

def test_compile_ok():
    response = client.post(
        '/bf_compiler',
        headers = {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Authorization'},
        json=test_json)
    assert response.status_code == 200
    assert response.json() == {'result':'Hello World!'}


def test_compile_ng():
    response = client.post(
        '/bf_compiler/api',
        headers={'Content-Type': 'application/json'},
        json={'bfcode':'+++++++'}
    )
    assert response.status_code == 404
    assert response.json() == {'detail':'Not Found'}


def test_text2bf():
    response = client.post(
        '/text_to_bfcode',
        headers = {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Authorization'},
        json={'text':'But I like it.'}
    )
    assert response.status_code == 200
    assert response.json() == {'result':'+++++++++++++++++[>++++>+++++++>+++++++>++>++++>++>++++++>++++++>++++++>++++++>++>++++++>+++++++>+++<<<<<<<<<<<<<<-]>--.>--.>---.>--.>+++++.>--.>++++++.>+++.>+++++.>-.>--.>+++.>---.>-----.>++++++++++++.'}