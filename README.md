# Vis.report
[_Visibility reports for divers to share conditions. Configured by default for Perth, Western Australia_](https://vis.report)

Written in python/html, using GeoDjango, PostGIS extension of Postgresql, and the Leaflet mapping library.
Started in January 2020 by Patrick Morrison

## Features

- Map interface to display reports, colour coded by the most recent visibility
- Detail pages for each site, with a full list of reports and an interface to add new ones.
- User accounts system with email authentication, and an admin page to add/edit dive sites. 
- A json api for using the data in other systems.

## Installation

Clone this repository, ake virtual environment, install requirements.txt and run with Django. You will also need a copy of postgres running on your system.

```bash
git clone https://github.com/PatrickMorrison1498/visreport.git
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
cd visreport
python manage.py runserver
```

## Usage

Go to 127.0.0.1:8000. It will be running there.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
