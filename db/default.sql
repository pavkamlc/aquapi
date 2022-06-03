INSERT INTO config (mqtt_host, mqtt_port, mqtt_topic, created) VALUES ('127.0.0.1', 1883, 'aquapi', datetime('now'));

INSERT INTO users (username, userpassword, created) VALUES ('admin', 'aquapi', datetime('now'));

INSERT INTO light (lightchannel, lightminute, lightvalue) VALUES (1, 1, 255);
INSERT INTO light (lightchannel, lightminute, lightvalue) VALUES (1, 1800, 127);
INSERT INTO light (lightchannel, lightminute, lightvalue) VALUES (1, 3599, 0);