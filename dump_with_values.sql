-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: CRICKET_TOURNAMENT
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AVAILABLE_PITCHES`
--
DROP DATABASE IF EXISTS `CRICKET_TOURNAMENT`;
CREATE DATABASE `CRICKET_TOURNAMENT`;
USE `CRICKET_TOURNAMENT`;

DROP TABLE IF EXISTS `AVAILABLE_PITCHES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AVAILABLE_PITCHES` (
  `GROUND_ID` int(10) NOT NULL,
  `PITCH_TYPE` varchar(10) NOT NULL,
  PRIMARY KEY (`GROUND_ID`,`PITCH_TYPE`),
  CONSTRAINT `AVAILABLE_PITCHES_ibfk_1` FOREIGN KEY (`GROUND_ID`) REFERENCES `GROUND` (`GROUND_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AVAILABLE_PITCHES`
--

LOCK TABLES `AVAILABLE_PITCHES` WRITE;
/*!40000 ALTER TABLE `AVAILABLE_PITCHES` DISABLE KEYS */;
INSERT INTO `AVAILABLE_PITCHES` VALUES (1,'dry'),(1,'green'),(1,'hard'),(2,'green'),(2,'hard'),(3,'green'),(4,'dry'),(4,'hard');
/*!40000 ALTER TABLE `AVAILABLE_PITCHES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CAPTAINS`
--

DROP TABLE IF EXISTS `CAPTAINS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CAPTAINS` (
  `CAPTAIN_ID` int(10) NOT NULL,
  `TEAM_ID` int(10) NOT NULL,
  PRIMARY KEY (`CAPTAIN_ID`,`TEAM_ID`),
  KEY `TEAM_ID` (`TEAM_ID`),
  CONSTRAINT `CAPTAINS_ibfk_1` FOREIGN KEY (`CAPTAIN_ID`) REFERENCES `PLAYER` (`PLAYER_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `CAPTAINS_ibfk_2` FOREIGN KEY (`TEAM_ID`) REFERENCES `TEAM` (`TEAM_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CAPTAINS`
--

LOCK TABLES `CAPTAINS` WRITE;
/*!40000 ALTER TABLE `CAPTAINS` DISABLE KEYS */;
INSERT INTO `CAPTAINS` VALUES (1,1),(11,2),(9,3);
/*!40000 ALTER TABLE `CAPTAINS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `COMMENTATOR`
--

DROP TABLE IF EXISTS `COMMENTATOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `COMMENTATOR` (
  `COMMENTATOR_ID` int(10) NOT NULL,
  `FIRST_NAME` varchar(20) NOT NULL,
  `MIDDLE_NAME` varchar(20) DEFAULT NULL,
  `LAST_NAME` varchar(20) NOT NULL,
  `DATE_OF_BIRTH` date DEFAULT NULL,
  PRIMARY KEY (`COMMENTATOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `COMMENTATOR`
--

LOCK TABLES `COMMENTATOR` WRITE;
/*!40000 ALTER TABLE `COMMENTATOR` DISABLE KEYS */;
INSERT INTO `COMMENTATOR` VALUES (1,'commfone','commmone','commlone','1984-03-21'),(2,'commftwo','commmtwo','commltwo','1978-01-01'),(3,'commfthree','commmthree','commlthree','1984-02-28');
/*!40000 ALTER TABLE `COMMENTATOR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GROUND`
--

DROP TABLE IF EXISTS `GROUND`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GROUND` (
  `GROUND_ID` int(10) NOT NULL,
  `NAME` varchar(20) NOT NULL,
  `LOCATION` varchar(20) NOT NULL,
  `CAPACITY` int(10) DEFAULT NULL,
  `LONGEST_BOUNDARY` int(5) DEFAULT NULL,
  `TEAM_ID` int(10) NOT NULL,
  PRIMARY KEY (`GROUND_ID`),
  KEY `TEAM_ID` (`TEAM_ID`),
  CONSTRAINT `GROUND_ibfk_1` FOREIGN KEY (`TEAM_ID`) REFERENCES `TEAM` (`TEAM_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GROUND`
--

LOCK TABLES `GROUND` WRITE;
/*!40000 ALTER TABLE `GROUND` DISABLE KEYS */;
INSERT INTO `GROUND` VALUES (1,'ground1','location1',50000,78,1),(2,'ground2','location2',45000,92,1),(3,'ground3','location3',52000,88,2),(4,'ground4','location4',49000,91,3);
/*!40000 ALTER TABLE `GROUND` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GROUND_USED`
--

DROP TABLE IF EXISTS `GROUND_USED`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GROUND_USED` (
  `TEAM_IDA` int(10) NOT NULL,
  `TEAM_IDB` int(10) NOT NULL,
  `GROUND_ID` int(10) NOT NULL,
  `DATE_AND_TIME` varchar(20) NOT NULL,
  PRIMARY KEY (`TEAM_IDA`,`TEAM_IDB`,`GROUND_ID`,`DATE_AND_TIME`),
  KEY `TEAM_IDB` (`TEAM_IDB`),
  KEY `GROUND_ID` (`GROUND_ID`),
  CONSTRAINT `GROUND_USED_ibfk_1` FOREIGN KEY (`TEAM_IDA`) REFERENCES `TEAM` (`TEAM_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `GROUND_USED_ibfk_2` FOREIGN KEY (`TEAM_IDB`) REFERENCES `TEAM` (`TEAM_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `GROUND_USED_ibfk_3` FOREIGN KEY (`GROUND_ID`) REFERENCES `GROUND` (`GROUND_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GROUND_USED`
--

LOCK TABLES `GROUND_USED` WRITE;
/*!40000 ALTER TABLE `GROUND_USED` DISABLE KEYS */;
INSERT INTO `GROUND_USED` VALUES (3,1,1,'01/05/2020 19:00'),(3,1,3,'25/04/2020 19:00'),(1,2,1,'21/04/2020 19:00'),(1,2,2,'27/04/2020 15:00'),(3,2,2,'23/04/2020 15:00'),(3,2,3,'29/04/2020 19:00');
/*!40000 ALTER TABLE `GROUND_USED` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MATCH_COMMENTATORS`
--

DROP TABLE IF EXISTS `MATCH_COMMENTATORS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MATCH_COMMENTATORS` (
  `TEAM_IDA` int(10) NOT NULL,
  `TEAM_IDB` int(10) NOT NULL,
  `COMMENTATOR_ID` int(10) NOT NULL,
  `DATE_AND_TIME` varchar(20) NOT NULL,
  PRIMARY KEY (`TEAM_IDA`,`TEAM_IDB`,`COMMENTATOR_ID`,`DATE_AND_TIME`),
  KEY `TEAM_IDB` (`TEAM_IDB`),
  KEY `COMMENTATOR_ID` (`COMMENTATOR_ID`),
  CONSTRAINT `MATCH_COMMENTATORS_ibfk_1` FOREIGN KEY (`TEAM_IDA`) REFERENCES `TEAM` (`TEAM_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `MATCH_COMMENTATORS_ibfk_2` FOREIGN KEY (`TEAM_IDB`) REFERENCES `TEAM` (`TEAM_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `MATCH_COMMENTATORS_ibfk_3` FOREIGN KEY (`COMMENTATOR_ID`) REFERENCES `COMMENTATOR` (`COMMENTATOR_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MATCH_COMMENTATORS`
--

LOCK TABLES `MATCH_COMMENTATORS` WRITE;
/*!40000 ALTER TABLE `MATCH_COMMENTATORS` DISABLE KEYS */;
INSERT INTO `MATCH_COMMENTATORS` VALUES (3,1,2,'01/05/2020 19:00'),(3,1,3,'25/04/2020 19:00'),(1,2,1,'21/04/2020 19:00'),(1,2,1,'27/04/2020 15:00'),(1,2,2,'21/04/2020 19:00'),(1,2,2,'27/04/2020 15:00'),(1,2,3,'27/04/2020 15:00'),(3,2,1,'29/04/2020 19:00'),(3,2,2,'23/04/2020 15:00'),(3,2,3,'23/04/2020 15:00');
/*!40000 ALTER TABLE `MATCH_COMMENTATORS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MATCH_REFEREES`
--

DROP TABLE IF EXISTS `MATCH_REFEREES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MATCH_REFEREES` (
  `TEAM_IDA` int(10) NOT NULL,
  `TEAM_IDB` int(10) NOT NULL,
  `REFEREE_ID` int(10) NOT NULL,
  `DATE_AND_TIME` varchar(20) NOT NULL,
  PRIMARY KEY (`TEAM_IDA`,`TEAM_IDB`,`REFEREE_ID`,`DATE_AND_TIME`),
  KEY `TEAM_IDB` (`TEAM_IDB`),
  KEY `REFEREE_ID` (`REFEREE_ID`),
  CONSTRAINT `MATCH_REFEREES_ibfk_1` FOREIGN KEY (`TEAM_IDA`) REFERENCES `TEAM` (`TEAM_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `MATCH_REFEREES_ibfk_2` FOREIGN KEY (`TEAM_IDB`) REFERENCES `TEAM` (`TEAM_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `MATCH_REFEREES_ibfk_3` FOREIGN KEY (`REFEREE_ID`) REFERENCES `REFEREE` (`REFEREE_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MATCH_REFEREES`
--

LOCK TABLES `MATCH_REFEREES` WRITE;
/*!40000 ALTER TABLE `MATCH_REFEREES` DISABLE KEYS */;
INSERT INTO `MATCH_REFEREES` VALUES (3,1,1,'01/05/2020 19:00'),(3,1,2,'01/05/2020 19:00'),(3,1,2,'25/04/2020 19:00'),(3,1,3,'25/04/2020 19:00'),(3,1,4,'01/05/2020 19:00'),(3,1,4,'25/04/2020 19:00'),(3,1,5,'01/05/2020 19:00'),(3,1,5,'25/04/2020 19:00'),(1,2,1,'21/04/2020 19:00'),(1,2,1,'27/04/2020 15:00'),(1,2,2,'21/04/2020 19:00'),(1,2,3,'21/04/2020 19:00'),(1,2,3,'27/04/2020 15:00'),(1,2,4,'21/04/2020 19:00'),(1,2,4,'27/04/2020 15:00'),(1,2,5,'27/04/2020 15:00'),(3,2,1,'23/04/2020 15:00'),(3,2,1,'29/04/2020 19:00'),(3,2,2,'23/04/2020 15:00'),(3,2,2,'29/04/2020 19:00'),(3,2,3,'23/04/2020 15:00'),(3,2,3,'29/04/2020 19:00'),(3,2,4,'23/04/2020 15:00'),(3,2,4,'29/04/2020 19:00'),(3,2,5,'23/04/2020 15:00'),(3,2,5,'29/04/2020 19:00');
/*!40000 ALTER TABLE `MATCH_REFEREES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PLAYER`
--

DROP TABLE IF EXISTS `PLAYER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PLAYER` (
  `PLAYER_ID` int(10) NOT NULL,
  `FIRST_NAME` varchar(20) NOT NULL,
  `MIDDLE_NAME` varchar(20) DEFAULT NULL,
  `LAST_NAME` varchar(20) NOT NULL,
  `DATE_OF_BIRTH` date DEFAULT NULL,
  `NATIONALITY` varchar(20) NOT NULL,
  `ROLE` varchar(20) NOT NULL,
  `MATCHES(BATTING)` int(5) DEFAULT NULL,
  `INNINGS(BATTING)` int(5) DEFAULT NULL,
  `RUNS(BATTING)` int(10) DEFAULT NULL,
  `AVERAGE(BATTING)` decimal(7,2) DEFAULT NULL,
  `HIGHEST_SCORE(BATTING)` int(5) DEFAULT NULL,
  `STRIKE_RATE(BATTING)` decimal(7,2) DEFAULT NULL,
  `MATCHES(BOWLING)` int(5) DEFAULT NULL,
  `INNINGS(BOWLING)` int(5) DEFAULT NULL,
  `WICKETS_TAKEN(BOWLING)` int(5) DEFAULT NULL,
  `AVERAGE(BOWLING)` decimal(7,2) DEFAULT NULL,
  `STRIKE_RATE(BOWLING)` decimal(7,2) DEFAULT NULL,
  `BEST_FIGURES(BOWLING)` varchar(15) DEFAULT NULL,
  `MATCHES(FIELDING)` int(5) DEFAULT NULL,
  `INNINGS(FIELDING)` int(5) DEFAULT NULL,
  `CATCHES(FIELDING)` int(5) DEFAULT NULL,
  `RUN_OUTS(FIELDING)` int(5) DEFAULT NULL,
  `CAPPED_STATUS` set('YES','NO') DEFAULT NULL,
  `MATCH_FEE` int(15) DEFAULT NULL,
  `AUCTIONED_PRICE` int(20) DEFAULT NULL,
  `TEAM_ID` int(10) DEFAULT NULL,
  PRIMARY KEY (`PLAYER_ID`),
  KEY `TEAM_ID` (`TEAM_ID`),
  CONSTRAINT `PLAYER_ibfk_1` FOREIGN KEY (`TEAM_ID`) REFERENCES `TEAM` (`TEAM_ID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PLAYER`
--

LOCK TABLES `PLAYER` WRITE;
/*!40000 ALTER TABLE `PLAYER` DISABLE KEYS */;
INSERT INTO `PLAYER` VALUES (1,'firstone',' middleone','lastone','1980-01-21','Indian','batsman',128,117,4720,40.34,90,134.45,128,9,10,49.00,47.00,'2-0-14-2',128,127,29,12,'YES',100000,170000000,1),(2,'firstwo','middletwo','lasttwo','1992-10-22','Indian','batsman',117,107,5374,50.22,122,142.55,117,5,9,42.00,46.00,'3-0-24-2',117,116,21,15,'YES',120000,95000000,2),(3,'firstthree','middlethree','lastthree','1984-04-04','England','batsman',173,129,4947,38.34,75,129.64,173,7,4,39.00,43.00,'4-0-43-3',173,172,15,9,'NO',900000,120000000,3),(4,'firstfour','middlefour','lastfour','1978-03-15','Indian','bowler',44,40,454,11.34,55,92.88,44,43,69,9.00,11.00,'7-1-39-5',44,43,15,21,'NO',100000,90000000,1),(5,'firstfive','middlefive','lastfive','1978-03-14','Indian','bowler',34,27,358,13.24,69,89.13,34,30,58,15.00,19.00,'8-2-34-5',34,33,14,19,'YES',120000,140000000,2),(6,'firstsix','middlesix','lastsix','1980-01-21','England','bowler',164,107,891,8.32,32,88.46,164,159,201,19.00,21.00,'6-1-43-4',164,163,18,25,'YES',900000,100000000,3),(7,'firstseven','middleseven','lastseven','1992-10-22','Indian','wicket keeper',97,93,2812,30.23,88,144.64,97,0,0,0.00,0.00,'0',97,96,23,35,'NO',100000,85000000,1),(8,'firsteight','middleeight','lasteight','1978-03-15','Indian','wicket keeper',70,69,2739,39.69,105,129.24,70,0,0,0.00,0.00,'0',70,69,27,27,'YES',120000,150000000,2),(9,'firstnine','middlenine','lastnine','1992-07-23','Sri Lanka','wicket keeper',75,70,2816,40.22,112,150.24,75,0,0,0.00,0.00,'0',75,74,29,41,'YES',900000,140000000,3),(10,'firstten','middleten','lastten','1978-12-11','Indian','all rounder',111,92,2599,28.24,93,140.35,111,86,81,29.00,27.00,'3-1-34-4',111,110,18,16,'YES',100000,110000000,1),(11,'firsteleven','middleeleven','lasteleven','1980-01-21','Indian','all rounder',146,63,1850,29.35,119,145.52,146,89,79,31.00,33.00,'4-0-24-2',146,145,24,21,'NO',120000,160000000,2),(12,'firsttwelve','middletwelve','lasttwelve','1984-04-04','Australia','all rounder',158,151,4980,32.98,79,120.53,158,97,102,35.00,32.00,'3-1-24-2',158,157,19,17,'YES',900000,130000000,3),(13,'firstthirteen','middlethirteen','lastthirteen','1980-07-08','Indian','all rounder',125,89,2840,31.90,81,146.35,125,93,103,27.00,32.00,'4-1-35-3',125,124,20,19,'YES',0,0,NULL);
/*!40000 ALTER TABLE `PLAYER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `REFEREE`
--

DROP TABLE IF EXISTS `REFEREE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `REFEREE` (
  `REFEREE_ID` int(10) NOT NULL,
  `FIRST_NAME` varchar(20) NOT NULL,
  `MIDDLE_NAME` varchar(20) DEFAULT NULL,
  `LAST_NAME` varchar(20) NOT NULL,
  `DATE_OF_BIRTH` date DEFAULT NULL,
  `NATIONALITY` varchar(20) NOT NULL,
  `SALARY` int(10) NOT NULL,
  `MATCHES_REFEREED_DOMESTICALLY` int(10) DEFAULT NULL,
  `MATCHES_REFEREED_INTERNATIONALLY` int(10) DEFAULT NULL,
  PRIMARY KEY (`REFEREE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `REFEREE`
--

LOCK TABLES `REFEREE` WRITE;
/*!40000 ALTER TABLE `REFEREE` DISABLE KEYS */;
INSERT INTO `REFEREE` VALUES (1,'reffone','refmone','reflone','1984-01-09','Indian',1500000,69,50),(2,'refftwo','refmtwo','refltwo','1978-08-06','West Indies',1100000,62,53),(3,'reffthree','refmthree','reflthree','1980-12-12','England',900000,57,61),(4,'refffour','refmfour','reflfour','1984-12-31','Indian',800000,47,48),(5,'reffive','refmive','reflive','1978-05-01','Indian',1700000,93,99);
/*!40000 ALTER TABLE `REFEREE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TEAM`
--

DROP TABLE IF EXISTS `TEAM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TEAM` (
  `TEAM_ID` int(10) NOT NULL,
  `NAME` varchar(20) NOT NULL,
  `OWNER_NAME` varchar(20) NOT NULL,
  `MATCHES_WON` int(5) DEFAULT NULL,
  `MATCHES_LOST` int(5) DEFAULT NULL,
  `MATCHES_DRAWN` int(5) DEFAULT NULL,
  `MATCHES_WITHOUT_A_RESULT` int(5) DEFAULT NULL,
  PRIMARY KEY (`TEAM_ID`),
  UNIQUE KEY `NAME` (`NAME`),
  UNIQUE KEY `OWNER_NAME` (`OWNER_NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TEAM`
--

LOCK TABLES `TEAM` WRITE;
/*!40000 ALTER TABLE `TEAM` DISABLE KEYS */;
INSERT INTO `TEAM` VALUES (1,'SRH','Kalanithi Maran',NULL,NULL,NULL,NULL),(2,'RCB','Vijay Maliya',NULL,NULL,NULL,NULL),(3,'CSK','N. Srinivasan',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `TEAM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TEAM_SPONSOR`
--

DROP TABLE IF EXISTS `TEAM_SPONSOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TEAM_SPONSOR` (
  `SPONSOR_ID` int(10) NOT NULL,
  `TEAM_ID` int(10) NOT NULL,
  `NAME` varchar(20) NOT NULL,
  `BUDGET` int(15) DEFAULT NULL,
  PRIMARY KEY (`SPONSOR_ID`,`TEAM_ID`),
  KEY `TEAM_SPONSOR_ibfk_1` (`TEAM_ID`),
  CONSTRAINT `TEAM_SPONSOR_ibfk_1` FOREIGN KEY (`TEAM_ID`) REFERENCES `TEAM` (`TEAM_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TEAM_SPONSOR`
--

LOCK TABLES `TEAM_SPONSOR` WRITE;
/*!40000 ALTER TABLE `TEAM_SPONSOR` DISABLE KEYS */;
INSERT INTO `TEAM_SPONSOR` VALUES (1,1,'sponsorone',500000000),(2,1,'sponsortwo',390000000),(3,2,'sponsorthree',690000000),(4,3,'sponsorfour',750000000);
/*!40000 ALTER TABLE `TEAM_SPONSOR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TEAM_SUPPORT_STAFF`
--

DROP TABLE IF EXISTS `TEAM_SUPPORT_STAFF`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TEAM_SUPPORT_STAFF` (
  `STAFF_ID` int(10) NOT NULL,
  `TEAM_ID` int(10) NOT NULL,
  `FIRST_NAME` varchar(20) NOT NULL,
  `MIDDLE_NAME` varchar(20) DEFAULT NULL,
  `LAST_NAME` varchar(20) NOT NULL,
  `SALARY` int(10) DEFAULT NULL,
  `ROLE_PLAYED` set('COACH','ADVISOR') DEFAULT NULL,
  `COACH_TYPE` set('HEAD','BATTING','FIELDING') DEFAULT NULL,
  `FIELD ADVISING` set('TEAM MANAGEMENT','FINANCIAL') DEFAULT NULL,
  PRIMARY KEY (`TEAM_ID`,`STAFF_ID`),
  CONSTRAINT `TEAM_SUPPORT_STAFF_ibfk_1` FOREIGN KEY (`TEAM_ID`) REFERENCES `TEAM` (`TEAM_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TEAM_SUPPORT_STAFF`
--

LOCK TABLES `TEAM_SUPPORT_STAFF` WRITE;
/*!40000 ALTER TABLE `TEAM_SUPPORT_STAFF` DISABLE KEYS */;
INSERT INTO `TEAM_SUPPORT_STAFF` VALUES (1,1,'sfone','smone','slone',1000000,'COACH','HEAD',NULL),(2,1,'shtwo','smtwo','sltwo',900000,'COACH','BATTING',NULL),(3,1,'sfthree','smthree','slthree',1000000,'ADVISOR',NULL,'FINANCIAL'),(4,2,'sffour','smfour','slfour',1200000,'COACH','HEAD',NULL),(5,2,'sffive','smfive','slfive',800000,'COACH','BATTING',NULL),(6,2,'sfsix','smsix','slsix',900000,'ADVISOR',NULL,'FINANCIAL'),(7,3,'sfseven','smseven','slseven',1200000,'COACH','HEAD',NULL),(8,3,'sfeight','smeight','sleight',1000000,'COACH','FIELDING',NULL),(9,3,'sfnine','smnine','slnine',900000,'ADVISOR',NULL,'TEAM MANAGEMENT');
/*!40000 ALTER TABLE `TEAM_SUPPORT_STAFF` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-12 21:18:58