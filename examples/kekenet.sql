-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 2019-11-19 15:06:57
-- 服务器版本： 10.1.34-MariaDB
-- PHP Version: 5.6.37

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kekenet`
--
CREATE DATABASE IF NOT EXISTS `kekenet` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `kekenet`;

-- --------------------------------------------------------

--
-- 表的结构 `article`
--

DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `id` bigint(20) NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `editor` varchar(30) DEFAULT NULL,
  `source` varchar(30) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  `txt_en` text,
  `txt_cn` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `article`
--

INSERT INTO `article` (`id`, `title`, `editor`, `source`, `datetime`, `txt_en`, `txt_cn`) VALUES
(1, '微软在日本试行4天工作制,工作效率暴增!', 'Kelly', 'chinadaily', '2019-11-06 18:06:00', 'A growing number of smaller companies are adopting a four-day workweek. Now the results of a recent trial at Microsoft (MSFT) suggest it could work even for the biggest businesses.', '越来越多中小公司开始采用四天工作制。如今微软近日的试验结果显示，就算在大企业也能见效。'),
(2, '你一开口,面试官就知道你是哪种人', 'Kelly', 'chinadaily', '2019-10-24 15:00:00', 'Job candidates are judged on their social status just a few seconds after they start to speak, according to a new study.', '一项新研究发现，求职者开口说话几秒钟后，面试官就已经对他们的社会地位做出了判断。'),
(3, '近一半的上班族因为压力太大而濒临崩溃', 'Kelly', 'chinadaily', '2019-10-12 07:00:00', 'Nearly half of all employees are close to \'breaking point\' at work due to increased stress levels. A survey of 2,000 professionals found the average working adult feels stressed for almost a third of their working day.', '近一半的上班族因为压力增大而濒临崩溃。一项针对2000名职场人士的研究发现：工作日期间，每位上班族平均有三分之一的时间感到心力交瘁。');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `article`
--
ALTER TABLE `article`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
