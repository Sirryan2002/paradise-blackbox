-- --------------------------------------------------------
-- Server version:               10.6.8-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

CREATE DATABASE IF NOT EXISTS `paradise_api_store` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `paradise_api_store`;

CREATE TABLE IF NOT EXISTS `data_anomalies` (
  `round_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `rounds` (
  `round_id` int(11) DEFAULT NULL,
  `round_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`round_data`)),
  `round_meta_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`round_meta_data`))
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
