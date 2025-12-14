# IERS Offline Cache Updater

This tool facilitates updating Astropy's IERS (International Earth Rotation and Reference Systems) data files in an offline environment.

Since Astropy v6.0, IERS data is managed by the [astropy-iers-data](https://github.com/astropy/astropy-iers-data) package. This tool helps you manually update these critical files when the machine running Astropy cannot access the internet.

## Usage

### Step 1: Acquire Data (Online Environment)

You need to obtain the key data files from a machine with internet access.

**Option A: Download from GitHub Releases (Recommended)**

Download the `iers-20XX-XX-XX.tar.gz` file from the [Latest Release](../../releases/tag/latest).

> **Note**: The release is built automatically on a weekly basis (every Sunday). It may not contain the data for the most recent few days. If you need real-time data, please use Option B.

**Option B: Generate Manually**

Clone this repository and run the update script manually:

```bash
git clone https://gitlab.com/jingyj/iers_cache.git
cd iers_cache
bash update_pack.sh
```

This will download the latest files (`eopc04_IAU2000.62-now`, `Leap_Second.dat`, `finals2000A.all`) and generate an archive file `iers-20XX-XX-XX.tar.gz`.

### Step 2: Install Data (Offline Environment)

1. Transfer the `iers-20XX-XX-XX.tar.gz` file to your offline machine.
2. Extract and run the update scripts:

```bash
tar -zxvf iers-20XX-XX-XX.tar.gz
cd iers
python gen_cache.py
python check.py
```

*   `gen_cache.py`: Sets up a temporary local server to feed the data to Astropy, updating its internal cache.
*   `check.py`: Verifies that the IERS data is correctly loaded and usable.
