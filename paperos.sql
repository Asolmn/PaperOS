/*
 Navicat Premium Data Transfer

 Source Server         : LOCALHOST
 Source Server Type    : MySQL
 Source Server Version : 50545
 Source Host           : localhost:3306
 Source Schema         : paperos

 Target Server Type    : MySQL
 Target Server Version : 50545
 File Encoding         : 65001

 Date: 24/12/2021 20:16:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version`  (
  `version_num` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`version_num`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('791b33d53092');

-- ----------------------------
-- Table structure for paper
-- ----------------------------
DROP TABLE IF EXISTS `paper`;
CREATE TABLE `paper`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `uuid` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `status` tinyint(1) NULL DEFAULT NULL,
  `student_id` int(11) NULL DEFAULT NULL,
  `path` varchar(265) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `uuid`(`uuid`) USING BTREE,
  INDEX `student_id`(`student_id`) USING BTREE,
  CONSTRAINT `paper_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of paper
-- ----------------------------
INSERT INTO `paper` VALUES (1, 'docx', '10e3cedb-cabb-40be-8619-98ea8472b3ef', 0, NULL, 'D:/Project/PaperOS/uploads\\10e3cedb-cabb-40be-8619-98ea8472b3ef.docx');
INSERT INTO `paper` VALUES (2, 'docx', 'e847c5f5-c3b4-4048-8052-388e56dc025c', 0, 1, 'D:/Project/PaperOS/uploads\\e847c5f5-c3b4-4048-8052-388e56dc025c.docx');
INSERT INTO `paper` VALUES (3, 'docx', 'cb639992-b58c-4abf-ab27-ef05d5127657', 0, 1, 'D:/Project/PaperOS/uploads\\cb639992-b58c-4abf-ab27-ef05d5127657.docx');
INSERT INTO `paper` VALUES (4, 'docx', 'e1d45d17-2285-4780-9cbb-4a34212c9f0c', 0, 1, 'D:/Project/PaperOS/uploads\\e1d45d17-2285-4780-9cbb-4a34212c9f0c.docx');
INSERT INTO `paper` VALUES (5, 'docx', '730e189c-6183-495d-a45a-a61bf4f15bd2', 0, 1, 'D:/Project/PaperOS/uploads\\730e189c-6183-495d-a45a-a61bf4f15bd2.docx');
INSERT INTO `paper` VALUES (6, 'docx', '28404d36-3bab-48a7-a230-19dff82ebdbe', 0, 1, 'D:/Project/PaperOS/uploads\\28404d36-3bab-48a7-a230-19dff82ebdbe.docx');
INSERT INTO `paper` VALUES (7, 'docx', 'f8e51fcd-42b5-4cc5-8661-339aaed18a79', 0, 1, 'D:/Project/PaperOS/uploads\\f8e51fcd-42b5-4cc5-8661-339aaed18a79.docx');
INSERT INTO `paper` VALUES (8, 'docx', '25e9e912-41b6-4e2c-8b70-e3cbe5c5c9e4', 0, 1, 'D:/Project/PaperOS/uploads\\25e9e912-41b6-4e2c-8b70-e3cbe5c5c9e4.docx');
INSERT INTO `paper` VALUES (9, 'stu.docx', '61ced2d9-6252-4be4-8836-28d1e68a69ac', 0, 1, 'D:/Project/PaperOS/uploads\\61ced2d9-6252-4be4-8836-28d1e68a69ac.docx');
INSERT INTO `paper` VALUES (10, 'docx', '57fcf5e9-57f0-4f33-affa-fbeb4e02b348', 0, 1, 'D:/Project/PaperOS/uploads\\57fcf5e9-57f0-4f33-affa-fbeb4e02b348.docx');
INSERT INTO `paper` VALUES (11, 's.docx', '0c8c1169-9ddb-4290-a1b3-4ec8fabf7b8a', 0, 1, 'D:/Project/PaperOS/uploads\\0c8c1169-9ddb-4290-a1b3-4ec8fabf7b8a.docx');

-- ----------------------------
-- Table structure for roles
-- ----------------------------
DROP TABLE IF EXISTS `roles`;
CREATE TABLE `roles`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `default` tinyint(1) NULL DEFAULT NULL,
  `permissions` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `ix_roles_default`(`default`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of roles
-- ----------------------------
INSERT INTO `roles` VALUES (1, 'Admin', 0, 0);
INSERT INTO `roles` VALUES (2, 'Student', 0, 0);
INSERT INTO `roles` VALUES (3, 'Teacher', 0, 0);

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `password` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `role_id` int(11) NULL DEFAULT NULL,
  `teacher_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `role_id`(`role_id`) USING BTREE,
  INDEX `teacher_id`(`teacher_id`) USING BTREE,
  CONSTRAINT `students_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `students_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES (1, 'stu1', '123', 2, 1);
INSERT INTO `students` VALUES (2, 'stu2', '123', 2, 1);
INSERT INTO `students` VALUES (4, 'stu3', '123', 2, 1);

-- ----------------------------
-- Table structure for teachers
-- ----------------------------
DROP TABLE IF EXISTS `teachers`;
CREATE TABLE `teachers`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `password` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `role_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `role_id`(`role_id`) USING BTREE,
  CONSTRAINT `teachers_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of teachers
-- ----------------------------
INSERT INTO `teachers` VALUES (1, 'tea1', '123', 3);

-- ----------------------------
-- Table structure for topics
-- ----------------------------
DROP TABLE IF EXISTS `topics`;
CREATE TABLE `topics`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topicname` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `uuid` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `student_id` int(11) NULL DEFAULT NULL,
  `status` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `topicname`(`topicname`) USING BTREE,
  UNIQUE INDEX `uuid`(`uuid`) USING BTREE,
  INDEX `student_id`(`student_id`) USING BTREE,
  CONSTRAINT `topics_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of topics
-- ----------------------------
INSERT INTO `topics` VALUES (2, '网易云', 'da02b582-0de9-37e2-83b4-fde91c513b97', 1, 1);
INSERT INTO `topics` VALUES (4, '毕业论文系统', 'b244ad56-eb5f-3df0-b637-28824c8139cf', 1, 0);
INSERT INTO `topics` VALUES (5, 'web编程4', '1790f844-5a3b-3e8d-9399-b71b4d3f511c', 1, 0);
INSERT INTO `topics` VALUES (6, '1', 'afd0b036-625a-3aa8-b639-9dc8c8fff0ff', NULL, 0);
INSERT INTO `topics` VALUES (12, 'web', 'dc57873b-9a7f-37df-b9c4-a10ee4509023', 1, 0);
INSERT INTO `topics` VALUES (13, 'web1', '67beaa8b-0d29-30f7-80b0-17de079dc0c7', 1, 0);

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `password` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `role_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ix_users_username`(`username`) USING BTREE,
  INDEX `role_id`(`role_id`) USING BTREE,
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of users
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
