import itertools
from datetime import date
sundays = sum(
	date(year, month, 1).weekday() == 6
	for year, month in itertools.product(range(1901, 2001), range(1, 13))
)
print(sundays)