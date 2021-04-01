CREATE DATABASE  IF NOT EXISTS `bank` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bank`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: bank
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account` (
  `CUST_ID` char(20) DEFAULT NULL,
  `ACC_NO` decimal(11,0) NOT NULL,
  `BALANCE` decimal(14,4) NOT NULL,
  `BRANCH_CODE` char(6) NOT NULL,
  PRIMARY KEY (`ACC_NO`),
  KEY `FK_ACCOUNT_CUSID` (`CUST_ID`),
  KEY `FK_BRANCH_BRCODE` (`BRANCH_CODE`),
  CONSTRAINT `FK_ACCOUNT_CUSID` FOREIGN KEY (`CUST_ID`) REFERENCES `customer` (`CUST_ID`) ON DELETE CASCADE,
  CONSTRAINT `FK_BRANCH_BRCODE` FOREIGN KEY (`BRANCH_CODE`) REFERENCES `branch` (`BRANCH_CODE`) ON DELETE CASCADE,
  CONSTRAINT `account_chk_1` CHECK ((`BALANCE` > 1000))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES ('CUS000001',3142000001,31532.0000,'BR01'),('CUS000002',3142000002,22050.0000,'BR02'),('CUS000003',3142000003,12000.0000,'BR01'),('CUS000004',3142000004,12475.0000,'BR03'),('CUS000005',3142000005,245682.0000,'BR01'),('CUS000006',3142000006,781235.0000,'BR03'),('CUS000007',3142000007,242552.0000,'BR02'),('CUS000008',3142000008,1478633.0000,'BR03'),('CUS000009',3142000009,4256.0000,'BR02'),('CUS0000010',31420000010,12345.0000,'BR01'),('CUS0000011',31420000011,365721.0000,'BR02'),('CUS0000012',31420000012,452413.0000,'BR03'),('CUS0000013',31420000013,2478.0000,'BR01'),('CUS0000014',31420000014,3698455.0000,'BR03');
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branch`
--

DROP TABLE IF EXISTS `branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branch` (
  `BRANCH_CODE` char(6) NOT NULL,
  `BRANCH_PLACE` varchar(10) NOT NULL,
  `MGR_ID` char(20) DEFAULT NULL,
  `IFSC_CODE` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`BRANCH_CODE`),
  KEY `MGR_ID` (`MGR_ID`),
  CONSTRAINT `branch_ibfk_1` FOREIGN KEY (`MGR_ID`) REFERENCES `employee` (`EMP_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch`
--

LOCK TABLES `branch` WRITE;
/*!40000 ALTER TABLE `branch` DISABLE KEYS */;
INSERT INTO `branch` VALUES ('BR01','BANGLORE','EMP000001','CBIN0000001'),('BR02','MYSORE','EMP000002','CBIN0000002'),('BR03','UDUPI','EMP000003','CBIN0000003');
/*!40000 ALTER TABLE `branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `CUST_ID` char(20) NOT NULL,
  `FIRST_NAME` varchar(15) NOT NULL,
  `LAST_NAME` varchar(15) DEFAULT NULL,
  `PLACE` varchar(15) DEFAULT NULL,
  `UID_NO` decimal(14,0) DEFAULT NULL,
  `MOB_NO` varchar(14) DEFAULT NULL,
  `EMAIL` varchar(30) NOT NULL,
  `PASSWD` char(35) NOT NULL,
  PRIMARY KEY (`CUST_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('CUS000001','Naveen','Trivikram','Banglore',697951775487,'9867759806','naveen@gmail.com','4b30474bc54230d7c530f60bea632805'),('CUS0000010','Sumanth','E U','Banglore',813776213145,'9798854756','sumanth@gmail.com','fc9d007c951e78f5267f8e81343d3bfe'),('CUS0000011','Vineeth','U','Mysore',587196709689,'9652709963','vineeth@gmail.com','a60460517acf7291eda26f6ebea8785c'),('CUS0000012','Pranav','Anvar','Udupi',572208452826,'9773260044','pranav@gmail.com','5bd33c004fa937b8da03e7b3f5f992c3'),('CUS0000013','Siddarth','Kashyap','Mysore',804042514374,'8409514653','siddarth@gmail.com','ddd9a2e254f567336cf62ab17754ded0'),('CUS0000014','Ragahav','L','Udupi',662796046464,'8445424474','ragahav@gmail.com','132e0e3ecec621df70fb7733c3bec67b'),('CUS000002','Ashwin','Shantilal','Mysore',55044984705,'8869546319','ashwin@gmail.com','9fd98753c4c0497aff3ab4521e507664'),('CUS000003','Pooja','K S','Banglore',507400847916,'8863944709','pooja@gmail.com','ca9b8720be925f9b038ca83faa1abcfe'),('CUS000004','Anirudh','C','Udupi',660147595093,'8691960972','anirudh@gmail.com','7c52b467085f6b08a8ee76276afadf67'),('CUS000005','Sandeep','T S','Banglore',454256365100,'9373927267','sandeep@gmail.com','405af813ccd7b73d3a386a010b0f1a63'),('CUS000006','Riya','Sanjay','Udupi',732626518107,'9601239898','riya@gmail.com','05134f2dcd5118a9e1f1c70423f825fa'),('CUS000007','Arjun','R','Mysore',724533459527,'8267052865','arjun@gmail.com','0083262ea4cc4844f65e804122e29cee'),('CUS000008','Fatima','F','Udupi',708801533932,'8517160234','fatima@gmail.com','3e52f4243a7cbac62fc05e016e097cee'),('CUS000009','Arya','Roa','Mysore',506590760717,'9572104899','arya@gmail.com','3483f8b04668b658c12023c84c55de4b');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `customer_details`
--

DROP TABLE IF EXISTS `customer_details`;
/*!50001 DROP VIEW IF EXISTS `customer_details`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `customer_details` AS SELECT 
 1 AS `CUST_ID`,
 1 AS `FIRST_NAME`,
 1 AS `LAST_NAME`,
 1 AS `MOB_NO`,
 1 AS `ACC_NO`,
 1 AS `BALANCE`,
 1 AS `BRANCH_CODE`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `customer_view`
--

DROP TABLE IF EXISTS `customer_view`;
/*!50001 DROP VIEW IF EXISTS `customer_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `customer_view` AS SELECT 
 1 AS `CUST_ID`,
 1 AS `FIRST_NAME`,
 1 AS `LAST_NAME`,
 1 AS `PLACE`,
 1 AS `MOB_NO`,
 1 AS `EMAIL`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `debit_card`
--

DROP TABLE IF EXISTS `debit_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `debit_card` (
  `ACC_NO` decimal(11,0) NOT NULL,
  `CARD_NO` decimal(18,0) NOT NULL,
  `EXPIRE_DATE` date NOT NULL,
  `CVV` decimal(4,0) NOT NULL,
  `PIN` decimal(6,0) NOT NULL,
  PRIMARY KEY (`CARD_NO`),
  KEY `FK_DEBITCARD_ACCNO` (`ACC_NO`),
  CONSTRAINT `FK_DEBITCARD_ACCNO` FOREIGN KEY (`ACC_NO`) REFERENCES `account` (`ACC_NO`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `debit_card`
--

LOCK TABLES `debit_card` WRITE;
/*!40000 ALTER TABLE `debit_card` DISABLE KEYS */;
INSERT INTO `debit_card` VALUES (3142000002,6362577592,'2021-08-08',123,1234),(3142000001,9686857541,'2021-08-08',123,1234);
/*!40000 ALTER TABLE `debit_card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `EMP_ID` char(20) NOT NULL,
  `NAME` varchar(15) NOT NULL,
  `EMAIL` varchar(30) NOT NULL,
  `PASSWD` char(35) NOT NULL,
  `BRANCH_CODE` char(6) DEFAULT NULL,
  `DESIGNATION` char(10) DEFAULT NULL,
  PRIMARY KEY (`EMP_ID`),
  KEY `FK_EMPLOYEE_BRANCHCODE` (`BRANCH_CODE`),
  CONSTRAINT `FK_EMPLOYEE_BRANCHCODE` FOREIGN KEY (`BRANCH_CODE`) REFERENCES `branch` (`BRANCH_CODE`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('EMP000001','Bushan Bhat','bushan@central.com','70ff3e7be2c918d0f2d135c8e046bbbb','BR01','Manager'),('EMP000002','Ravi Shankar','ravishankar@central.com','723b0b86d0c2b08de89d7f8349421a10','BR02','Manager'),('EMP000003','Sathish G','sathish@central.com','72a408866531a23769cee2c0c3e95d5b','BR03','Manager'),('EMP000004','Anith','anitha@central.com','399ed9a2556941551d54a1db42e33765','BR01','TELLER'),('EMP000005','Vivek','vivek@central.com','df79ed05cfd15da5eabce82daaff66a0','BR02','TELLER'),('EMP000006','Rmesh Kaur','ramesh@central.com','deefa505665eb2f51aa2c106f4efbb35','BR03','TELLER'),('emp100','HARSHA','harsha@gmail,com','70ff3e7be2c918d0f2d135c8e046bbbb','BR02','TELLER');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `transaction_details`
--

DROP TABLE IF EXISTS `transaction_details`;
/*!50001 DROP VIEW IF EXISTS `transaction_details`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `transaction_details` AS SELECT 
 1 AS `TRANS_ID`,
 1 AS `FROM_ACC`,
 1 AS `TO_ACC`,
 1 AS `TIME_DATE`,
 1 AS `TYPE_OF_TRANS`,
 1 AS `AMOUNT`,
 1 AS `STATUS`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `TRANS_ID` char(10) NOT NULL,
  `FROM_ACC` decimal(11,0) DEFAULT NULL,
  `TO_ACC` decimal(11,0) DEFAULT NULL,
  `TIME_DATE` timestamp NULL DEFAULT NULL,
  `TYPE_OF_TRANS` char(10) DEFAULT NULL,
  `AMOUNT` decimal(10,5) DEFAULT NULL,
  `REMARKS` varchar(100) DEFAULT NULL,
  `STATUS` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`TRANS_ID`),
  KEY `FK_TRANSACTION_ACCNO1` (`FROM_ACC`),
  KEY `FK_TRANSACTION_ACCNO2` (`TO_ACC`),
  CONSTRAINT `FK_TRANSACTION_ACCNO1` FOREIGN KEY (`FROM_ACC`) REFERENCES `account` (`ACC_NO`) ON DELETE CASCADE,
  CONSTRAINT `FK_TRANSACTION_ACCNO2` FOREIGN KEY (`TO_ACC`) REFERENCES `account` (`ACC_NO`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES ('TR000001',3142000001,3142000002,'2021-01-22 15:24:51','IMPS',254.00000,'offer','SUCCESS'),('TR000002',3142000002,3142000001,'2021-01-22 15:24:51','NEFT',4500.00000,'DEED','SUCCESS'),('TR000003',3142000001,3142000002,'2021-01-22 15:24:51','IMPS',170.00000,'offer','SUCCESS'),('TR000004',3142000002,3142000001,'2021-01-22 15:24:51','NEFT',45789.00000,'GIST','SUCCESS'),('TR000005',3142000001,3142000002,'2021-01-22 15:24:51','RTGS',2536.00000,'REWARD','SUCCESS'),('TR000006',3142000004,3142000005,'2021-01-13 13:07:31','NEFT',11000.00000,'offer','SUCCESS'),('TR000007',3142000006,3142000004,'2021-01-13 13:07:31','NEFT',500.00000,'deed','SUCCESS'),('TR000008',3142000006,3142000005,'2021-01-13 07:07:31','NEFT',110.00000,'gift','SUCCESS'),('TR000009',3142000005,3142000006,'2021-01-13 07:07:31','NEFT',1452.00000,'for use','SUCCESS'),('TR000010',3142000004,3142000006,'2021-01-13 07:07:31','NEFT',14567.00000,' ','SUCCESS'),('TR000011',3142000007,3142000008,'2021-01-12 07:07:31','NEFT',100.00000,'Money','SUCCESS'),('TR000012',3142000008,3142000009,'2021-01-12 07:07:31','NEFT',30.00000,'your use','SUCCESS'),('TR000013',3142000009,3142000007,'2021-01-12 07:07:31','NEFT',500.00000,' ','SUCCESS'),('TR000014',3142000007,3142000009,'2021-01-12 07:07:31','NEFT',100.00000,'Gift','SUCCESS'),('TR000015',3142000009,3142000008,'2021-01-12 07:07:31','NEFT',100.00000,' ','SUCCESS'),('TR000016',31420000010,31420000011,'2021-01-11 07:07:31','NEFT',100.00000,'Gift','SUCCESS'),('TR000017',31420000011,31420000012,'2021-01-11 07:07:31','NEFT',200.00000,'deed','SUCCESS'),('TR000018',31420000010,31420000012,'2021-01-11 07:07:31','NEFT',52.00000,'offer','SUCCESS'),('TR000019',31420000012,31420000010,'2021-01-11 07:07:31','NEFT',34.00000,'For house','SUCCESS'),('TR000020',31420000011,31420000012,'2021-01-11 07:07:31','NEFT',57.00000,'for loan','SUCCESS'),('TR000021',3142000002,3142000001,'2021-02-03 15:50:32','RTGS',200.00000,'To : vasudeva,Transaction remarks For loan, Mob No: 9686857541','FAILED'),('TR000022',3142000001,3142000002,'2021-02-03 15:51:51','NEFT',200.00000,'To : shiva,Transaction remarks For education, Mob No: 9686857541','SUCCESS'),('TR000023',3142000001,3142000002,'2021-02-03 16:07:57','NEFT',5000.00000,'To : vasudeva,Transaction remarks for rent, Mob No: 9686857541','SUCCESS'),('TR000024',3142000002,3142000001,'2021-02-03 16:10:22','NEFT',600.00000,'To : Naveen,Transaction remarks For usage, Mob No: 9686857541','SUCCESS'),('TR000025',3142000002,3142000001,'2021-02-03 17:04:51','NEFT',40.00000,'To : vasudeva,Transaction remarks For education, Mob No: 9686857541','SUCCESS'),('TR000026',3142000001,3142000002,'2021-02-03 17:04:56','RTGS',1000.00000,'To : vasudeva,Transaction remarks For usage, Mob No: 968685712','SUCCESS'),('TR000027',3142000002,3142000001,'2021-02-04 02:20:02','RTGS',1000.00000,'To : ramakrishna,Transaction remarks For usage, Mob No: 9686857541','SUCCESS'),('TR000028',3142000001,3142000002,'2021-02-04 02:20:07','RTGS',2000.00000,'To : vasudeva,Transaction remarks For loan, Mob No: 9686857541','SUCCESS'),('TR000029',3142000001,3142000002,'2021-02-04 05:46:20','RTGS',200.00000,'To : vasudeva,Transaction remarks For education, Mob No: 9686857541','SUCCESS'),('TR000030',3142000002,3142000001,'2021-02-04 05:46:25','RTGS',2000.00000,'To : ramakrishna,Transaction remarks For usage, Mob No: 9686857541','SUCCESS');
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `customer_details`
--

/*!50001 DROP VIEW IF EXISTS `customer_details`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `customer_details` AS select `customer`.`CUST_ID` AS `CUST_ID`,`customer`.`FIRST_NAME` AS `FIRST_NAME`,`customer`.`LAST_NAME` AS `LAST_NAME`,`customer`.`MOB_NO` AS `MOB_NO`,`account`.`ACC_NO` AS `ACC_NO`,`account`.`BALANCE` AS `BALANCE`,`account`.`BRANCH_CODE` AS `BRANCH_CODE` from (`customer` join `account` on((`customer`.`CUST_ID` = `account`.`CUST_ID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `customer_view`
--

/*!50001 DROP VIEW IF EXISTS `customer_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `customer_view` AS select `customer`.`CUST_ID` AS `CUST_ID`,`customer`.`FIRST_NAME` AS `FIRST_NAME`,`customer`.`LAST_NAME` AS `LAST_NAME`,`customer`.`PLACE` AS `PLACE`,`customer`.`MOB_NO` AS `MOB_NO`,`customer`.`EMAIL` AS `EMAIL` from `customer` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `transaction_details`
--

/*!50001 DROP VIEW IF EXISTS `transaction_details`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `transaction_details` AS select `transactions`.`TRANS_ID` AS `TRANS_ID`,`transactions`.`FROM_ACC` AS `FROM_ACC`,`transactions`.`TO_ACC` AS `TO_ACC`,`transactions`.`TIME_DATE` AS `TIME_DATE`,`transactions`.`TYPE_OF_TRANS` AS `TYPE_OF_TRANS`,`transactions`.`AMOUNT` AS `AMOUNT`,`transactions`.`STATUS` AS `STATUS` from `transactions` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-27 18:34:47
