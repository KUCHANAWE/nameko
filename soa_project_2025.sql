-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 19, 2025 at 12:09 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `soa_project_2025`
--

-- --------------------------------------------------------

--
-- Table structure for table `kitchen_tasks`
--

CREATE TABLE `kitchen_tasks` (
  `kitchen_task_id` bigint(20) UNSIGNED NOT NULL,
  `kitchen_id` bigint(20) UNSIGNED NOT NULL,
  `menu` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `chef` varchar(255) DEFAULT NULL,
  `status` enum('pending','cooking','done') NOT NULL DEFAULT 'pending',
  `notes` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `kitchen_tasks`
--

INSERT INTO `kitchen_tasks` (`kitchen_task_id`, `kitchen_id`, `menu`, `quantity`, `chef`, `status`, `notes`, `created_at`, `updated_at`) VALUES
(1, 1, 'Nasi Goreng', 2, 'Chef Budi', 'pending', 'Tidak pedas', '2025-06-15 20:39:23', '2025-06-15 20:39:23'),
(2, 2, 'Mie Ayam', 1, 'Chef Sari', 'cooking', NULL, '2025-06-15 20:39:23', '2025-06-15 20:39:23'),
(3, 3, 'Sate Ayam', 3, NULL, 'done', 'Tambahkan sambal', '2025-06-15 20:39:23', '2025-06-15 20:39:23');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kitchen_tasks`
--
ALTER TABLE `kitchen_tasks`
  ADD PRIMARY KEY (`kitchen_task_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kitchen_tasks`
--
ALTER TABLE `kitchen_tasks`
  MODIFY `kitchen_task_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
