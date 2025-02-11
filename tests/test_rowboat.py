import pytest
from src.models.rowboat import Rowboat


class TestRowboat:
    @pytest.fixture
    def boat(self):
        return Rowboat(capacity=4, material="wood")

    def test_initial_state(self, boat):
        assert boat.capacity == 4
        assert boat.material == "wood"
        assert boat.position == (0, 0)
        assert not boat.is_moving

    def test_movement(self, boat):
        boat.change_direction("east")
        boat.move()
        assert boat.position == (1, 0)
        assert boat.is_moving

    def test_passenger_management(self, boat):
        for _ in range(4):
            boat.add_passenger()
        with pytest.raises(ValueError):
            boat.add_passenger()

        for _ in range(4):
            boat.remove_passenger()
        with pytest.raises(ValueError):
            boat.remove_passenger()

    def test_direction_change(self, boat):
        boat.change_direction("south")
        assert boat.direction == "south"

    def test_stop_boat(self, boat):
        boat.move()
        boat.stop()
        assert not boat.is_moving
