DROP DATABASE IF EXISTS demand_forecasting;

CREATE DATABASE demand_forecasting;

USE demand_forecasting;

CREATE TABLE user(
  id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(50) NOT NULL
);