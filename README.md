## Step 1. 

On a computer with public Internet connection.

```bash
$ git clone https://gitlab.com/jingyj/iers_cache.git
$ cd iers_cache
$ bash update_pack.sh
```
`update_pack.sh` will download (overwrite if exists) file: `eopc04_IAU2000.62-now`, `Leap_Second.dat` and `finals2000A.all`,
and generate an Archive File `iers-20XX-XX-XX.tar.gz`.

## Step 2.

Uploading the Archive File `iers-20XX-XX-XX.tar.gz` onto the computer without public Internet connection.
```bash
$ tar -zxvf iers-20XX-XX-XX.tar.gz
$ cd iers
$ python gen_cache.py
$ python check.py
```
