import io
import json
import pytest
from PIL import Image
import base64
import colorCorrection




@pytest.fixture
def client():
    with colorCorrection.test_client() as client:
        yield client


def test_upload(client):
    # Load the test image
    with open("test_image.png", "rb") as f:
        img_bytes = f.read()
    img_base64 = base64.b64encode(img_bytes).decode("utf-8")

    # Make a request to the API
    data = {
        "photo": (io.BytesIO(img_bytes), "test_image.png"),
        "option": "Protanopia"
    }
    response = client.post("/api/upload", data=data)

    # Check the response status code
    assert response.status_code == 200

    # Check the response image
    img = Image.open(io.BytesIO(response.data))
    assert img.format == "PNG"
    assert img.size == (256, 256)
