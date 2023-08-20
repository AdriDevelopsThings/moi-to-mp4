class MoiFileTime:
    def __init__(self, year, month, day, hour, minutes, seconds) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
    
    def __str__(self) -> str:
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.month} {self.seconds}ms"

def read_moi_file_time(filename):
    with open(filename, "rb") as file:
        file.seek(6)
        year = int.from_bytes(file.read(2), "big")
        month = int.from_bytes(file.read(1), "big")
        day = int.from_bytes(file.read(1), "big")
        hour = int.from_bytes(file.read(1), "big")
        minutes = int.from_bytes(file.read(1), "big")
        seconds = int.from_bytes(file.read(2), "big")

        return MoiFileTime(year, month, day, hour, minutes, seconds)