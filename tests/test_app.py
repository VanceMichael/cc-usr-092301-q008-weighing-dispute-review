from app import app


def test_health_endpoint_reports_service_status():
    response = app.test_client().get('/health')

    assert response.status_code == 200
    assert response.get_json() == {'status': 'ok'}
