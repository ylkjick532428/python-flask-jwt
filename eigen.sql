/*
 Navicat Premium Data Transfer

 Source Server         : eigen
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : localhost:3306
 Source Schema         : eigen

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : 65001

 Date: 05/12/2017 20:27:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '文章id',
  `user_id` varchar(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP,
  `modify_time` timestamp(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `stat` int(2) NOT NULL DEFAULT 1 COMMENT '文章状态, 1正常,0删除',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of article
-- ----------------------------
INSERT INTO `article` VALUES (1, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 19:54:02', NULL, 1);
INSERT INTO `article` VALUES (2, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 19:55:30', NULL, 1);
INSERT INTO `article` VALUES (3, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 19:57:03', '2017-12-05 20:04:06', 0);
INSERT INTO `article` VALUES (4, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 19:57:04', '2017-12-05 19:59:31', 0);
INSERT INTO `article` VALUES (5, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 19:57:07', NULL, 1);
INSERT INTO `article` VALUES (6, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:04:52', NULL, 1);
INSERT INTO `article` VALUES (7, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:04:55', '2017-12-05 20:05:02', 0);
INSERT INTO `article` VALUES (8, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:04:55', '2017-12-05 20:05:44', 0);
INSERT INTO `article` VALUES (9, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:04:55', '2017-12-05 20:06:14', 0);
INSERT INTO `article` VALUES (10, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:04:56', NULL, 1);
INSERT INTO `article` VALUES (11, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:07:00', NULL, 1);
INSERT INTO `article` VALUES (12, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:07:00', '2017-12-05 20:09:24', 0);
INSERT INTO `article` VALUES (13, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:07:01', NULL, 1);
INSERT INTO `article` VALUES (14, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:07:01', NULL, 1);
INSERT INTO `article` VALUES (15, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:07:01', NULL, 1);
INSERT INTO `article` VALUES (16, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:07:01', NULL, 1);
INSERT INTO `article` VALUES (17, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:07:01', NULL, 1);
INSERT INTO `article` VALUES (18, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:07:02', NULL, 1);
INSERT INTO `article` VALUES (19, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:07:02', NULL, 1);
INSERT INTO `article` VALUES (20, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:07:02', NULL, 1);
INSERT INTO `article` VALUES (21, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:07:02', NULL, 1);
INSERT INTO `article` VALUES (22, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:07:03', NULL, 1);
INSERT INTO `article` VALUES (23, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:07:03', NULL, 1);
INSERT INTO `article` VALUES (24, '8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'dfhdfdfiads地方还是短发的覅撒地方还是发', '2017-12-05 20:07:03', NULL, 1);

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role`  (
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '权限名称',
  `permission` int(2) NOT NULL COMMENT '权限值\r\nUSER = 1\r\nADMIN = 2',
  `id` int(2) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES ('USER', 1, 7);
INSERT INTO `role` VALUES ('ADMIN', 2, 8);
INSERT INTO `role` VALUES ('DEFAULT', 1, 9);

-- ----------------------------
-- Table structure for test
-- ----------------------------
DROP TABLE IF EXISTS `test`;
CREATE TABLE `test`  (
  `id` int(11) NOT NULL,
  `username` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(120) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of test
-- ----------------------------
INSERT INTO `test` VALUES (1, 'my_new_email@example.com', '32');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` varchar(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户id',
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '用户名',
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '密码',
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '电子邮件',
  `role_id` int(2) NOT NULL COMMENT '权限',
  `register_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP COMMENT '注册时间',
  `login_time` timestamp(0) NULL DEFAULT NULL COMMENT '登录时间\r\n',
  `access_token` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'token',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('137fca6a-7052-4635-b47b-233fa1029fea', 'jick122', 'pbkdf2:sha256:50000$IFMexhzc$c0693ff762d97a725d24e342b893d213e62897c4b92a1869d7ed13ca7f1e01a3', '', 8, '2017-12-05 18:57:04', '2017-12-05 20:07:54', NULL);
INSERT INTO `users` VALUES ('8b5d05a0-3ee2-479d-b9dc-68920237c249', 'jick12234', 'pbkdf2:sha256:50000$liVCSG1U$d549eb2faea28f7bc5495b6cf01a3a27496c1a7eff72dd0c20f598c20eb3aab2', '', 7, '2017-12-05 19:10:08', '2017-12-05 19:10:08', NULL);
INSERT INTO `users` VALUES ('8fadd4d3-eae2-4b2c-9641-ecb17099139c', 'jick', 'pbkdf2:sha256:50000$bZTodmL2$130fe18bba5be58e72c80ef61b68ecb3cdd6cce08976e47788da9699a50a7d61', 'jick@jick.com', 7, '2017-12-05 18:38:12', '2017-12-05 19:51:47', NULL);
INSERT INTO `users` VALUES ('9e290318-65b6-4960-a457-59b5910581a1', 'jick1223', 'pbkdf2:sha256:50000$nvEMfuCa$a5bae81b6a0949b9f39617b57ad4f3332bb8e5ba4edbbf91a310dbfdf8286d2b', '', 7, '2017-12-05 18:57:34', '2017-12-05 18:57:34', NULL);
INSERT INTO `users` VALUES ('aa22199c-be76-48fa-8698-eb90ed944ab6', 'jick1', 'pbkdf2:sha256:50000$RRc5jAfy$655f63d6518889dcd9849d7e494e5127bc84c592a4fa79123fea8f637ede613d', '', 7, '2017-12-05 18:52:40', NULL, NULL);
INSERT INTO `users` VALUES ('b25d96a0-feec-43ad-9ab9-135c062d4c99', 'jick12', 'pbkdf2:sha256:50000$DeL8fGBL$465d9482b6d2b51c77dc4b45902d3cadeee868c00df90c7fba1e0d2116964e00', '', 7, '2017-12-05 18:52:54', NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
