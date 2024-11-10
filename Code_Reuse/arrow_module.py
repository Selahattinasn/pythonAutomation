import arrow
date=arrow.get('2023-11-24', 'YYYY-MM-DD')
gun=date.shift(weeks=+6).format('MMM DD YYYY')
print(gun)