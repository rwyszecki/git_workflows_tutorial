class Job:
    @staticmethod
    def addition(*args: int) -> int:
        result = 0
        for number in args:
            result += number
        return result
