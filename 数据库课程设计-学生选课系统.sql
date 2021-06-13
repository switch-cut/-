/*
 Navicat MySQL Data Transfer

 Source Server         : 测试
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : 数据库课程设计-学生选课系统

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 10/06/2021 20:17:14
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `Aid` int(0) NOT NULL COMMENT '管理员id',
  `Apsd` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '管理员密码',
  PRIMARY KEY (`Aid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES (1001, 'admin');
INSERT INTO `admin` VALUES (1002, 'admin');
INSERT INTO `admin` VALUES (1003, 'admin');

-- ----------------------------
-- Table structure for selection
-- ----------------------------
DROP TABLE IF EXISTS `selection`;
CREATE TABLE `selection`  (
  `Sid` int(0) NOT NULL COMMENT '学号',
  `Jid` int(0) NOT NULL COMMENT '课程号',
  PRIMARY KEY (`Sid`, `Jid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of selection
-- ----------------------------
INSERT INTO `selection` VALUES (20001, 1);
INSERT INTO `selection` VALUES (20001, 2);
INSERT INTO `selection` VALUES (20001, 3);
INSERT INTO `selection` VALUES (20001, 4);
INSERT INTO `selection` VALUES (20001, 6);
INSERT INTO `selection` VALUES (20002, 2);
INSERT INTO `selection` VALUES (20002, 7);

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students`  (
  `Sid` int(0) NOT NULL AUTO_INCREMENT COMMENT '学生学号',
  `Sname` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '学生姓名',
  `Sage` int(0) NOT NULL COMMENT '学生年龄',
  `Ssex` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '性别',
  `Stele` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '电话',
  PRIMARY KEY (`Sid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20023 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES (20001, '小孙', 21, '男', '17658386515');
INSERT INTO `students` VALUES (20002, '小史', 21, '男', '17658386515');
INSERT INTO `students` VALUES (20003, '小吴', 22, '男', '17658386515');
INSERT INTO `students` VALUES (20004, '小高', 21, '男', '17658386515');
INSERT INTO `students` VALUES (20005, '小马', 20, '男', '17658386515');
INSERT INTO `students` VALUES (20006, '小沙', 20, '男', '17658386515');
INSERT INTO `students` VALUES (20007, '小孔', 22, '男', '17658386515');
INSERT INTO `students` VALUES (20008, '小王', 23, '男', '17658386515');
INSERT INTO `students` VALUES (20009, '小李', 19, '男', '17658386515');
INSERT INTO `students` VALUES (20010, '小邵', 20, '女', '17658386515');
INSERT INTO `students` VALUES (20011, '小代', 20, '女', '17658386515');
INSERT INTO `students` VALUES (20012, '小华', 19, '女', '17658386515');
INSERT INTO `students` VALUES (20013, '小赵', 20, '女', '17658386515');
INSERT INTO `students` VALUES (20014, '小邱', 20, '女', '17658386515');
INSERT INTO `students` VALUES (20021, '小江', 24, '男', '17658386527');

-- ----------------------------
-- Table structure for subject
-- ----------------------------
DROP TABLE IF EXISTS `subject`;
CREATE TABLE `subject`  (
  `Jid` int(0) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '课程号',
  `Jname` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '课程名称',
  `Jcredit` int(0) NOT NULL COMMENT '学分',
  PRIMARY KEY (`Jid`, `Jname`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of subject
-- ----------------------------
INSERT INTO `subject` VALUES (1, '数据库', 2);
INSERT INTO `subject` VALUES (2, '操作系统', 2);
INSERT INTO `subject` VALUES (3, '数字电路', 2);
INSERT INTO `subject` VALUES (4, '计算机网络', 2);
INSERT INTO `subject` VALUES (5, '计算机导论', 2);
INSERT INTO `subject` VALUES (6, '概率论', 2);
INSERT INTO `subject` VALUES (7, '大学英语', 2);
INSERT INTO `subject` VALUES (8, '网页设计', 2);
INSERT INTO `subject` VALUES (9, 'Java编程', 2);
INSERT INTO `subject` VALUES (10, 'PS设计', 2);

SET FOREIGN_KEY_CHECKS = 1;
