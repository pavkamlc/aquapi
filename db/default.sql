INSERT INTO config ('mqtt_host', 'mqtt_port', 'mqtt_topic', 'created') VALUES ('127.0.0.1', 1883, 'aquapi', datetime('now'));

INSERT INTO users (username, userpassword) VALUES ('admin', 'aquapi');