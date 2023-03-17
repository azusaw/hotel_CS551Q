INSERT INTO disaster_continent (id) VALUES
	 ('Africa'),
	 ('Americas'),
	 ('Asia'),
	 ('Europe'),
	 ('Oceania')
;


INSERT INTO disaster_region (id, continent_id) VALUES
	 ('WesternAfrica','Africa'),
	 ('SouthernAfrica','Africa'),
	 ('EasternAfrica','Africa'),
	 ('NorthernAfrica','Africa'),
	 ('MiddleAfrica','Africa'),
	 ('SouthAmerica','Americas'),
	 ('NorthernAmerica','Americas'),
	 ('Caribbean','Americas'),
	 ('CentralAmerica','Americas'),
	 ('WesternAsia','Asia'),
	 ('SouthernAsia','Asia'),
	 ('EasternAsia','Asia'),
	 ('CentralAsia','Asia'),
	 ('South-Eastern-Asia','Asia'),
	 ('WesternEurope','Europe'),
	 ('SouthernEurope','Europe'),
	 ('EasternEurope','Europe'),
	 ('NorthernEurope','Europe'),
	 ('RussianFederation', 'Europe'),
	 ('AustraliaandNewZealand','Oceania'),
	 ('Melanesia','Oceania'),
	 ('Micronesia','Oceania'),
	 ('Polynesia','Oceania')
;

INSERT INTO disaster_type (id) VALUES
	 ('Flood'),
	 ('Storm'),
	 ('Drought'),
	 ('Animal-accident'),
	 ('Earthquake'),
	 ('Epidemic'),
	 ('Extreme-temperature'),
	 ('Glacial-lake-outbrust'),
	 ('Impact'),
	 ('Insect-infestation'),
	 ('Landslide'),
	 ('Mass-movement(dry)'),
	 ('Volcanic-activity'),
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



