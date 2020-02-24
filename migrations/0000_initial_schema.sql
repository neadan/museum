create schema museum;

create table city (
	name varchar(100),
	country varchar(100),
	population bigint,
	CONSTRAINT city_pkey PRIMARY KEY (name)
);

create table museum (
	name varchar(100),
	yearlyvisitors bigint,
	city varchar(100),
	CONSTRAINT museum_pkey PRIMARY KEY (name),
    CONSTRAINT museum_city_fkey FOREIGN KEY (city) REFERENCES city (name)
);