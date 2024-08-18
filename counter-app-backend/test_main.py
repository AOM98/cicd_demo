# test_main.py

import pytest
from httpx import AsyncClient
from main import app, counter  # Import app and counter from main.py


@pytest.fixture(autouse=True)
def reset_counter():
    """
    This fixture ensures that the counter is reset before each test.
    """
    counter.value = 0


@pytest.mark.asyncio
async def test_get_counter_initial_value():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/counter")
    assert response.status_code == 200
    assert response.json() == {"value": 0}


@pytest.mark.asyncio
async def test_increment_counter():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/counter/increment")
    assert response.status_code == 200
    assert response.json() == {"value": 1}


@pytest.mark.asyncio
async def test_decrement_counter():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Increment the counter first
        await ac.post("/counter/increment")
        # Then decrement the counter
        response = await ac.post("/counter/decrement")
    assert response.status_code == 200
    assert response.json() == {"value": 0}


@pytest.mark.asyncio
async def test_reset_counter():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Increment the counter first
        await ac.post("/counter/increment")
        # Reset the counter
        response = await ac.post("/counter/reset")
    assert response.status_code == 200
    assert response.json() == {"value": 0}
