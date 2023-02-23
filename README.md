# aquapi
Aquarium control from raspberry
Plugins in folder plugins capable

Hardware:
Rasperry PI zero W - controller
Waweshare ePaper Hat - display information
Waveshare motor driver HAT - control led ligths 4CH
Custom GPIO HA - measure watter temperature, air temperature, watter level, control heater, control intake valve, control alarm siren

Implemented:
Web service in flask
Displaying information
Light harmonogram

Requirements:
python modules - time, sqlite3, flask, flask_login, flask_wtf, wtforms, config, app