#!/usr/bin/env python

from astropy.utils.iers import conf
from astropy.time import Time
from datetime import datetime
print(Time(datetime.now(), format='datetime').ut1)
