-- MySQL dump 10.14  Distrib 5.5.68-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: students
-- ------------------------------------------------------
-- Server version	5.5.68-MariaDB

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
-- Table structure for table `base`
--

DROP TABLE IF EXISTS `base`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base` (
  `stuid` varchar(10) NOT NULL COMMENT '学号',
  `name` varchar(10) NOT NULL COMMENT '姓名',
  `sex` varchar(2) NOT NULL COMMENT '性别',
  `native` varchar(10) NOT NULL COMMENT '籍贯',
  `nation` varchar(20) NOT NULL COMMENT '民族',
  `birth` varchar(10) NOT NULL COMMENT '出生年月',
  `high` varchar(5) NOT NULL COMMENT '身高',
  `weigh` varchar(5) NOT NULL COMMENT '体重（公斤）',
  `education` varchar(10) NOT NULL COMMENT '学历',
  `school` varchar(30) NOT NULL COMMENT '毕业院校',
  `tele` varchar(30) NOT NULL COMMENT '电话',
  `QQ` varchar(30) NOT NULL COMMENT 'QQ',
  `linkman` varchar(50) NOT NULL COMMENT '紧急联系人及电话',
  `comedate` varchar(50) NOT NULL COMMENT '入班日期',
  PRIMARY KEY (`stuid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base`
--

LOCK TABLES `base` WRITE;
/*!40000 ALTER TABLE `base` DISABLE KEYS */;
INSERT INTO `base` VALUES ('2214101','小张','男','武汉','汉','20000101','181','75','大专','北京化工大学','18511111111','168661212','张爸','20220901'),('2214102','小李','男','北京','汉','','','','','','','','',''),('2214103','小王','女','西安','','','','','','','','','','');
/*!40000 ALTER TABLE `base` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chengji`
--

DROP TABLE IF EXISTS `chengji`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chengji` (
  `stud_no` varchar(10) NOT NULL,
  `hardware` char(10) DEFAULT NULL,
  `software` char(10) DEFAULT NULL,
  `network` char(10) DEFAULT NULL,
  `english` char(10) DEFAULT NULL,
  `type` char(10) DEFAULT NULL COMMENT ' 打字成绩',
  `RAID` char(10) DEFAULT NULL COMMENT 'RAID实践',
  `wire` char(10) DEFAULT NULL COMMENT '网线制作',
  `BIOS` char(10) DEFAULT NULL COMMENT 'BIOS设定',
  `sysinstall` char(10) DEFAULT NULL COMMENT '系统安装',
  `sysmanager` char(10) DEFAULT NULL COMMENT 'windows系统管理',
  `netmanager` char(10) DEFAULT NULL COMMENT '网络故障排查',
  `VISIO` char(10) DEFAULT NULL COMMENT 'VISIO画架构图',
  PRIMARY KEY (`stud_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='\r\n';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chengji`
--

LOCK TABLES `chengji` WRITE;
/*!40000 ALTER TABLE `chengji` DISABLE KEYS */;
/*!40000 ALTER TABLE `chengji` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `courses` (
  `cid` varchar(4) NOT NULL COMMENT '课程ID',
  `coursename` varchar(20) DEFAULT NULL COMMENT '课程名或实践考核名称',
  `ctype` varchar(1) DEFAULT NULL COMMENT '理论（0）or 实践（1）',
  `clevel` varchar(1) DEFAULT NULL COMMENT '1-计算机基础 2-linux基础'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES ('1001','硬件组成','理','1'),('1002','软件组成','理','1'),('1003','网络基础','理','1'),('1004','英语','理','1'),('1101','打字速度','实','1'),('1102','磁盘RAID','实','1'),('1103','网线制作','实','1'),('1104','BIOS设置','实','1'),('1105','系统安装','实','1'),('1106','系统管理','实','1'),('1107','网线管理','实','1'),('1108','VISIO机柜图','实','1');
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `score`
--

DROP TABLE IF EXISTS `score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `score` (
  `stuid` varchar(10) DEFAULT NULL COMMENT '学号',
  `coursename` varchar(20) DEFAULT NULL COMMENT '课程名或实践考核名称',
  `score` varchar(10) DEFAULT NULL COMMENT '分数或优良级'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `score`
--

LOCK TABLES `score` WRITE;
/*!40000 ALTER TABLE `score` DISABLE KEYS */;
INSERT INTO `score` VALUES ('2214101','硬件组成','10'),('2214101','软件组成','10'),('2214102','硬件组成','8'),('2214103','软件组成','9');
/*!40000 ALTER TABLE `score` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-08  5:31:17
