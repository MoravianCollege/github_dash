# git_dash

This repo contains a [Dash](https://dash.plot.ly/) dashboard
that displays stats for Github repos.


## Production Setup

* Image an SD card with [Screenly OSE](https://www.screenly.io/ose/) (use [Etcher](https://www.balena.io/etcher/))
* Create a file `/boot/ssh` on the SD Card (see #3 from the [SSH page](https://www.raspberrypi.org/documentation/remote-access/ssh/README.md))
* Boot the Pi.  Screenly will launch to a screen that shows the IP
* Connect using the IP: `ssh pi@<IP>` Password is `raspberry`
* Change the password: `sudo passwd pi`
* Update the package manager: `sudo apt-get update`
* Install pip3: `sudo apt-get install python3-pip`
* Install [gunicorn](https://gunicorn.org/): `sudo pip3 install gunicorn`
* Clone this repo to the Pi (and go into the directory)
* Install the dependencies (as root): `sudo pip3 install -r requirements.txt`
* Create a file named `.env` that contains `GITHUB_TOKEN=<TOKEN>` (replace `<TOKEN>` with a [GitHub Personal Access Token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line) with `repo` access)
* Note the name of the directory: `pwd`
* Edit `/etc/rc.local` and add the following *above* `exit 0`: (Replace `<repo dir>` with the absolute path 
  and note the `&` at the end of each line!)
   ```
   python3 <repo dir>/src/github_collect/collector.py &
   gunicorn --chdir  <repo dir>/src/github_dash app:app.server &
   ``` 
   
* Reboot: `sudo reboot`
* Point a web browser at `http://<Pi IP>`
* Add the dashboard as an asset: `http://localhost:8000`
* Turn on the dashboard asset (and remove the default assets)
* Under settings, disable "Show spash screen" so the IP is not shown at boot.  Click "Save Settings" to save
* Reboot again