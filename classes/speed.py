class SpeedConverted():
    
    def get_speed_from_pace(self, pace: str) -> dict:
        """ get speed from pace """
        minutes, seconds = pace.split(':')
        total_second_per_km = int(seconds) + (int(minutes) * 60)

        return {'speed': round(3600 / total_second_per_km, 2)}

    def get_pace_from_speed(self, speed: str) -> dict:
        """ get pace from speed """
        speed = float(speed)

        seconds_speed = (1 / speed * 60)*60
        minutes_speed = int((seconds_speed//60))

        return {'minutes': minutes_speed, 'seconds': round(seconds_speed % 60)}