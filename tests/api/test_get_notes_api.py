import pytest
import time
from pages.api.notes import NotesAPI


@pytest.mark.api
@pytest.mark.order(8)

def test_get_all_notes(headers):

    notes_api = NotesAPI()

    start_time = time.time()

    response = notes_api.get_all_notes(headers)

    response_time = time.time() - start_time

    # Validate status code
    assert response.status_code == 200

    response_json = response.json()

    # Validate notes list
    assert "data" in response_json
    assert isinstance(response_json["data"], list)

    # Validate response time
    assert response_time < 2, f"Response time exceeded: {response_time:.2f} sec"
