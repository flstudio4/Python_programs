-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: contacts
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `contact_entries`
--

DROP TABLE IF EXISTS `contact_entries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact_entries` (
  `id` int NOT NULL AUTO_INCREMENT,
  `l_name` varchar(45) DEFAULT NULL,
  `f_name` varchar(45) DEFAULT NULL,
  `work_number` varchar(45) DEFAULT NULL,
  `cellphone_number` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `zip` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=528 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_entries`
--

LOCK TABLES `contact_entries` WRITE;
/*!40000 ALTER TABLE `contact_entries` DISABLE KEYS */;
INSERT INTO `contact_entries` VALUES (1,'Sumenko','Dmitrii',NULL,'7735678798',NULL,NULL,NULL,NULL,NULL),(2,'Woods','Anthony',NULL,'3456789890',NULL,NULL,NULL,NULL,NULL),(3,'Blackburn','Landon',NULL,'7734567654',NULL,NULL,NULL,NULL,NULL),(4,'Kwakye','Lillian',NULL,'7734563423',NULL,NULL,NULL,NULL,NULL),(5,'May','Andy',NULL,'7734561234',NULL,NULL,NULL,NULL,NULL),(6,'Tate','Allison',NULL,'7732356576',NULL,NULL,NULL,NULL,NULL),(7,'Wu','Jacky',NULL,'7734568796',NULL,NULL,NULL,NULL,NULL),(8,'Morrison','Julia',NULL,'2345678796',NULL,NULL,NULL,NULL,NULL),(9,'Dwornik','Thomas',NULL,'3453456587',NULL,NULL,NULL,NULL,NULL),(10,'Hlebnikova','Marina',NULL,'7735346575',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `contact_entries` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-13  4:22:37
