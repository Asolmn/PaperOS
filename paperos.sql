-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: paperos
-- ------------------------------------------------------
-- Server version	8.0.29-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `paper`
--

DROP TABLE IF EXISTS `paper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paper` (
  `id` int NOT NULL AUTO_INCREMENT,
  `filename` varchar(128) NOT NULL,
  `uuid` varchar(128) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `path` varchar(265) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `student_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `paper_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`),
  CONSTRAINT `paper_chk_1` CHECK ((`status` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper`
--

LOCK TABLES `paper` WRITE;
/*!40000 ALTER TABLE `paper` DISABLE KEYS */;
INSERT INTO `paper` VALUES (1,'docx','51761875-3f5c-46b4-8b71-8ba3a836b21c',1,'D:\\Project\\PaperOS\\uploads\\51761875-3f5c-46b4-8b71-8ba3a836b21c.docx','2022-04-14 00:03:06',1),(2,'docx','42c35926-30cf-448e-be00-a29e0d4ff890',0,'/root/project/PaperOS/uploads/42c35926-30cf-448e-be00-a29e0d4ff890.docx','2022-06-03 22:45:28',2),(3,'docx','02e0bab3-2b1e-4e95-a996-d72d0c95872f',0,'/root/project/PaperOS/uploads/02e0bab3-2b1e-4e95-a996-d72d0c95872f.docx','2022-06-03 22:45:28',NULL),(4,'docx','ca7b8894-8d4f-4c31-b17c-6a8f7d73d0a0',0,'/root/project/PaperOS/uploads/ca7b8894-8d4f-4c31-b17c-6a8f7d73d0a0.docx','2022-06-03 22:45:28',NULL),(5,'docx','35353c8d-d3e2-4075-81a7-b9f226d8b772',0,'/root/project/PaperOS/uploads/35353c8d-d3e2-4075-81a7-b9f226d8b772.docx','2022-06-03 22:45:28',NULL),(6,'docx','2eb1e71f-c651-4da9-b3e8-9e37669e2043',0,'/root/project/PaperOS/uploads/2eb1e71f-c651-4da9-b3e8-9e37669e2043.docx','2022-06-03 22:45:28',NULL),(7,'docx','b6ee4900-57c3-41a6-a175-3d3640f990ad',0,'/root/project/PaperOS/uploads/b6ee4900-57c3-41a6-a175-3d3640f990ad.docx','2022-06-03 22:45:28',NULL),(8,'docx','d8f1281e-5d63-4170-acd8-9eff2d6fd115',0,'/root/project/PaperOS/uploads/d8f1281e-5d63-4170-acd8-9eff2d6fd115.docx','2022-06-03 22:45:28',NULL),(9,'docx','b3ca7df4-720f-4505-a644-195f8c2d1c3b',0,'/root/project/PaperOS/uploads/b3ca7df4-720f-4505-a644-195f8c2d1c3b.docx','2022-06-03 22:45:28',NULL),(10,'docx','2b08e496-5334-4872-a82f-6c806ca5223b',0,'/root/project/PaperOS/uploads/2b08e496-5334-4872-a82f-6c806ca5223b.docx','2022-06-03 22:45:28',NULL),(11,'docx','9a864262-11ea-416a-95ed-4cb942a7b6af',0,'/root/project/PaperOS/uploads/9a864262-11ea-416a-95ed-4cb942a7b6af.docx','2022-06-03 22:45:28',NULL),(12,'docx','64e4b8bf-f101-4017-978d-1993f33f81e4',1,'/root/project/PaperOS/uploads/64e4b8bf-f101-4017-978d-1993f33f81e4.docx','2022-06-03 22:45:28',1),(13,'docx','6f7ac521-0d55-4666-b695-384f7891788e',0,'/root/project/PaperOS/uploads/6f7ac521-0d55-4666-b695-384f7891788e.docx','2022-06-03 22:45:28',NULL),(14,'docx','48a0f55c-548f-4be0-8479-42f7889986dc',0,'/root/project/PaperOS/uploads/48a0f55c-548f-4be0-8479-42f7889986dc.docx','2022-06-03 22:45:28',1),(15,'test.docx','9b15eff8-b28f-4689-a17f-acab54e188b5',1,'/root/project/PaperOS/uploads/9b15eff8-b28f-4689-a17f-acab54e188b5.docx','2022-06-13 19:25:29',1),(16,'docx','cea6ead6-1ba2-4c3b-8dfc-f0776c28ba34',0,'/root/project/PaperOS/uploads/cea6ead6-1ba2-4c3b-8dfc-f0776c28ba34.docx','2022-06-13 19:25:29',2),(21,'docx','a744a783-f1cd-4879-bc7e-d2ee49393766',0,'/root/project/PaperOS/uploads/a744a783-f1cd-4879-bc7e-d2ee49393766.docx','2022-06-13 19:25:29',2),(22,'docx','4b382640-7ee0-47bf-bbc7-5cf707f794cb',1,'/root/project/PaperOS/uploads/4b382640-7ee0-47bf-bbc7-5cf707f794cb.docx','2022-06-13 19:25:29',7),(23,'docx','b2a77593-563f-4ec1-b377-729039df2688',0,'/root/project/PaperOS/uploads/b2a77593-563f-4ec1-b377-729039df2688.docx','2022-06-13 19:25:29',7),(24,'student.docx','b851c2e8-b40b-44b9-a10b-87e8e6af5ad6',0,'/root/project/PaperOS/uploads/b851c2e8-b40b-44b9-a10b-87e8e6af5ad6.docx','2022-06-13 19:25:29',7),(25,'paper.docx','b17e59ca-b4b8-49fe-80be-d20c39437d65',0,'/root/project/PaperOS/uploads/b17e59ca-b4b8-49fe-80be-d20c39437d65.docx','2022-06-13 19:25:29',7),(26,'paper.docx','07153e47-ca9f-4a8d-b59a-db3e63339220',0,'/root/project/PaperOS/uploads/07153e47-ca9f-4a8d-b59a-db3e63339220.docx','2022-06-13 19:25:29',7);
/*!40000 ALTER TABLE `paper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `default` tinyint(1) DEFAULT NULL,
  `permissions` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_roles_default` (`default`),
  CONSTRAINT `roles_chk_1` CHECK ((`default` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Admin',0,0),(2,'Teacher',0,0),(3,'Student',0,0),(4,'Test',0,0),(5,'Test1',0,0);
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `role_id` int DEFAULT NULL,
  `teacher_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `role_id` (`role_id`),
  KEY `teacher_id` (`teacher_id`),
  CONSTRAINT `students_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`),
  CONSTRAINT `students_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'stu1','123',3,3),(2,'stu2','123',2,3),(7,'stu3','123',3,3),(8,'stu4','123',3,NULL),(9,'stu5','123',3,NULL);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `role_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `teachers_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (1,'tea1','123',2),(3,'tea2','123',2),(4,'tea3','123',2);
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `topics`
--

DROP TABLE IF EXISTS `topics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `topics` (
  `id` int NOT NULL AUTO_INCREMENT,
  `topicname` varchar(128) NOT NULL,
  `uuid` varchar(128) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `student_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `topicname` (`topicname`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `topics_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`),
  CONSTRAINT `topics_chk_1` CHECK ((`status` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topics`
--

LOCK TABLES `topics` WRITE;
/*!40000 ALTER TABLE `topics` DISABLE KEYS */;
INSERT INTO `topics` VALUES (1,'毕业论文管理系统','09209e65-34ee-39b7-a8aa-90aead7a1f72',1,1),(2,'学生管理系统','a097e22d-219e-312e-8d18-5e091d0190f9',1,1),(7,'论文管理系统','79a2d34d-2f11-3cce-bf93-618acd1055dd',0,1),(15,'毕业论文系统','b244ad56-eb5f-3df0-b637-28824c8139cf',0,1),(17,'管理系统','a8a2b728-a3de-3da9-9746-e61312e47aca',0,1),(28,'毕业系统管理','49e2eea1-7191-352a-bbe1-f74ed20b1f85',1,2),(29,'毕业设计系统1','da02b582-0de9-37e2-83b4-fde91c513b97',1,7),(31,'毕业设计系统2','73b73fae-0802-3b5c-a9ca-ee3bdf6c2efe',0,7);
/*!40000 ALTER TABLE `topics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `role_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_username` (`username`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'adm1','123',1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-15 21:07:10
