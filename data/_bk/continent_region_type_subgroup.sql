INSERT INTO disaster_continent (id) VALUES
	 ('Africa'),
	 ('Americas'),
	 ('Asia'),
	 ('Europe'),
	 ('Oceania')
;


INSERT INTO disaster_region (id, continent_id) VALUES
	 ('Western Africa','Africa'),
	 ('Southern Africa','Africa'),
	 ('Eastern Africa','Africa'),
	 ('Northern Africa','Africa'),
	 ('Middle Africa','Africa'),
	 ('South America','Americas'),
	 ('Northern America','Americas'),
	 ('Caribbean','Americas'),
	 ('Central America','Americas'),
	 ('Western Asia','Asia'),
	 ('Southern Asia','Asia'),
	 ('Eastern Asia','Asia'),
	 ('Central Asia','Asia'),
	 ('South-Eastern Asia','Asia'),
	 ('Western Europe','Europe'),
	 ('Southern Europe','Europe'),
	 ('Eastern Europe','Europe'),
	 ('Northern Europe','Europe'),
	 ('Australia and New Zealand','Oceania'),
	 ('Melanesia','Oceania'),
	 ('Micronesia','Oceania'),
	 ('Polynesia','Oceania')
;

INSERT INTO disaster_type (id) VALUES
	 ('Flood'),
	 ('Storm'),
	 ('Drought'),
	 ('Animal accident'),
	 ('Eathquake'),
	 ('Epidemic'),
	 ('Extreme temprature'),
	 ('Glacial lake outbrust'),
	 ('Impact'),
	 ('Insect infestation'),
	 ('Landslide'),
	 ('Mass movement (dry)'),
	 ('Volcanic activity'),
	 ('Wildfire')
;

INSERT INTO disaster_subgroup (id) VALUES
	 ('Hydrogical'),
	 ('Meteological'),
	 ('Climatological'),
	 ('Geophysical'),
	 ('Biological'),
	 ('Extra-terrestrial')
;



