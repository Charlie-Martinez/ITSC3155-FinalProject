from fastapi import HTTPException
from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import orders as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_track_order(db_session):
    """Test that a tracking number returns the full order"""

    order_data = {
        "id": 1,
        "customer_id": 1,
        "customer_name": "John Doe",
        "description": "Double cheeseburger with no onions",
        "tracking_number": "TRK123ABC",
        "order_status": "Pending",
        "delivery_type": "delivery",
        "total_price": 6.99,
        "promotion_id": None,
        "order_date": "2020-04-01"
    }
    mock_order = model.Order(**order_data)
    db_session.query.return_value.filter.return_value.first.return_value = mock_order

    result = controller.read_by_tracking(db_session, "TRK123ABC")
    assert result is not None
    assert result.tracking_number == "TRK123ABC"
    assert result.customer_name == "John Doe"
    assert result.total_price == 6.99