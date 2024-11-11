def convert(seconds):
    hours=seconds//3600
    minutes= (seconds - hours*3600) // 60
    remaining= (seconds - hours*3600 - minutes*60)
    return hours, minutes, remaining

hours, minutes, seconds = convert(5000)
print(hours, minutes, seconds)