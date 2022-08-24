## On a computer with public Internet connection.

```bash
$ git clone https://gitlab.com/jingyj/iers_cache.git
$ cd iers_cache
$ bash update_pack.sh
```
`update_pack.sh` will download (overwrite if exists) file: `eopc04_IAU2000.62-now`, `Leap_Second.dat` and `finals2000A.all`,
and generate an Archive File `iers-XXX.tar.gz`.

## On the computer without public Internet connection.
uploading the Archive File `iers-XXX.tar.gz` onto it.
```bash
$ tar -zxvf iers-XXX.tar.gz
$ cd iers
$ python gen_cache.py
$ python check.py
```
