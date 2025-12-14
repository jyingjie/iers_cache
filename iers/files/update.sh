#!/bin/bash
set -e

# https://github.com/astropy/astropy/blob/v5.0.x/astropy/utils/iers/data/update_builtin_iers.sh
# iers.IERS_B_URL
wget http://hpiers.obspm.fr/iers/eop/eopc04/eopc04_IAU2000.62-now -O eopc04_IAU2000.62-now
# iers.IERS_LEAP_SECOND_URL
wget https://hpiers.obspm.fr/iers/bul/bulc/Leap_Second.dat -O Leap_Second.dat
# https://github.com/astropy/astropy/blob/main/astropy/utils/iers/iers.py
# IERS-A
wget https://datacenter.iers.org/data/9/finals2000A.all -O finals2000A.all
