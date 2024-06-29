from classes.speed import SpeedConverted

class TestClasses:
    def test_calculate_speed_from_pace(self):
        """ Test calculate speed_from_pace """
        s = SpeedConverted()
        assert s.get_speed_from_pace('4:40') == {'speed': 12.86}, "wrong speed from pace"

    def test_calculate_pace_from_speed(self):
        """ Test calculate pace from speed """
        s = SpeedConverted()
        assert s.get_pace_from_speed('13') == {'minutes': 4, 'seconds': 37}, "wrong pace from speed"