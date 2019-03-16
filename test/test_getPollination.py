import pytest

from .TestConnexion import TestConnexion


@pytest.mark.usefixtures('client')
class TestRequest(TestConnexion):
    """A test to get pollination from the monitoring api
    """

    def test_getPollination(self, client):
        request = {
            'type': 'event_Pollution',
            'payload': {
                'region': 'Mainfranken',
                'day': 'today'
            }
        }

        response = client.post('api/v1/request', json=request)

        assert response.status_code == 200
        print(response.get_json())
