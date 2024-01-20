create database CAD_Clothzy;
use CAD_Clothzy;
create table Clothzy_User_REG (
SNO int not null,
USER_ID int primary key,
FIRST_NAME varchar(255),
LAST_NAME varchar(255),
USER_NAME varchar(255),
GENDER varchar(255),
AGE long,
EMAIL varchar(225),
CONTACT_NO long not null,
ADDRESS varchar(255),
PASSWORD varchar(255) default 'Pasword@321',
CONFIRM_PASSWORD varchar(255) default'Password@321'
);
insert into Clothzy_User_Reg(SNO,USER_ID,FIRST_NAME,LAST_NAME,USER_NAME,GENDER,AGE,EMAIL,CONTACT_NO,ADDRESS)
values
(1,1001,'AARIF','S','@aarif01','MALE',25,'aarif01cad@gmail.com',9025171297,'MADURAI'),
(2,1002,'ABDUL RAHMAN','A','@abdul01','MALE',19,'abdulrahmancad01@gmail.com',9042116396,'TRICHY'),
(3,1003,'ABINAYA','J','@abinaya03','FEMALE',19,'abinayakumarcad01@gmail.com',8124568273,'SRIRANGAM'),
(4,1004,'AHAMED','J','@ahamed04','MALE',21,'ahamedcad01@gmail.com',9659021407,'TRICHY'),
(5,1005,'ALEXANDAR','A','@alex05','MALE',22,'alexandaracad01@gmail.com',9360415014,'KEERANUR'),
(6,1006,'ANAND','R','@anand06','MALE',27,'anandravichandrancad01@gmail.com',8489903993,'TRICHY'),
(7,1007,'ANJUKA','P','@anjuka06','FEMALE',21,'anjukapugaz02@gmail.com',6379944693,'TRICHY'),
(8,1008,'ARAVIND','K','@aravind08','MALE',24,'aravind2k23cad01@gmail.com',8778624466,'TRICHY'),
(9,1009,'BASHEER AHAMED','M','basheer09','MALE',21,'basheercad01@gmail.com',9514690405,'TRICHY'),
(10,1010,'CHANDRAN','P','@chandran10','MALE',22,'chandrancad01@gmail.com',9361313775,'KARUR'),
(11,1011,'DANIELRAJ','A','@daniel11','MALE',24,'danielrajcad01@gmail.com',9092838116,'THANJAVUR'),
(12,1012,'DINESH','T','@dinesh12','MALE',24,'tdineshcad01@gmail.com',9629724889,'TRICHY'),
(13,1013,'DOMENIG VASANTHAN','A','@vassanthan13','MALE',25,'vasanthcad01@gmail.com',8220904749,'TRICHY'),
(14,1014,'GOPAL','S','gopal14','MALE',22,'gopalcad01@gmail.com',9361448297,'KARUR'),
(15,1015,'HARSH','A','@harsh15','MALE',20,'harshcad01@gmail.com',9025664587,'TRICHY'),
(16,1016,'JAYAPRAVIN','D','@pravin16','MALE',22,'jayapravincad01@gmail.com',7094937902,'TRICHY'),
(17,1017,'JEMIMAH','J','@jemimah17','FEMALE ',22,'jemimahcad01@gmail.com',9489189043,'TRICHY'),
(18,1018,'MANIMOHANA','S','2mohana18','FEMALE ',26,'Mohanacad01@gmail.com',9994987424,'TRICHY'),
(19,1019,'KIRUTHIGA','R','@kiruthiga19','FEMALE ',26,'kiruthigarcad01@gmail.com',7339220870,'TRICHY'),
(20,1020,'NANCY','A','@nancy20','FEMALE ',24,'nancyacad01@gmail.com',8428267221,'PUDUKKOTTAI'),
(21,1021,'NATRAYAN','M','@natryan21','MALE',26,'natrayancad01@gmail.com',8825684098,'TRICHY'),
(22,1022,'PAVITHRA','K','@pavithra22','FEMALE ',21,'pavithracad01@gmail.com',9025862493,'TRICHY'),
(23,1023,'PRABHAHARN','M','@prabaharan23','MALE',29,'prabhaharncad01@gmail.com',9043792705,'TRICHY'),
(24,1024,'RAMKI','S','@ramki24','MALE',23,'ramkisridharcad01@gmail.com',6383693933,'TRICHY'),
(25,1025,'SAHITH AFRIDI','SABIBULLA','@afridi25','MALE',22,'sahithcad01@gmail.com',9042314497,'TRICHY'),
(26,1026,'SAKTHIVEL','S','@sakthi26','MALE',20,'jerrycad01@gmail.com',9514605031,'PERAMBALUR'),
(27,1027,'SANJAY','BALAKRISHNAN','@sanjay27','MALE',22,'sanjayrbcad01@gmail.com',7708407173,'TRICHY'),
(28,1028,'SANTHOSH KUMAR','S','@santhosh28','MALE',21,'santhoshcad01@gmail.Com',9344560546,'TRICHY'),
(29,1029,'SARAN','S','MALE',21,'@saran29','sarancad01@gmail.com',6380026784,'CUDDALORE'),
(30,1030,'SIRANJEEVI','S','@siranjeevi30','MALE',22,'siranjeevicad01@gmail.com',6383685553,'PERAMBALUR');
 
select * from Clothzy_User_REG;

CREATE TABLE Clothzy_User_LOGIN(
LOGIN_ID int primary key auto_increment,
USER_ID int not null,
USER_NAME varchar(255) NOT NULL unique,
PASSWORD varchar(255) NOT null,
foreign key(USER_ID)references Clothzy_user_Reg (USER_ID)
);
select * from Clothzy_User_LOGIN;

INSERT INTO CLOTHZY_USER_LOGIN(USER_ID,USER_NAME,PASSWORD) SELECT USER_ID,USER_NAME,PASSWORD FROM CLOTHZY_USER_REG;
TRUNCATE TABLE clothzy_User_LOGIN;
create table clothzy_User_Order(
 PRODUCT_NO varchar(255) not null unique,
 ORDER_ID long,
 PRICE  double,
 DELIVERY_LOCATION varchar(255),
 USER_ID int not null,
 foreign key(USER_ID)references Clothzy_user_Reg (USER_ID)
);
select *from CLOTHZY_User_Order;
create table Clothzy_User_PROMOTION(
SNO int not null,
VINTAGE_COLLECTIONS varchar(255),
WEDDING_COLLECTIONS varchar(255),
FORMAL_OUTFITS varchar(255),
SEMIFORMAL_OUTFITS varchar(255),
SUMMER_COLLECTIONS varchar(255),
WINTER_COLLECTIONS varchar(255)
);
insert into clothzy_user_promotion(SNO,VINTAGE_COLLECTIONS,WEDDING_COLLECTIONS,
FORMAL_OUTFITS,SEMIFORMAL_OUTFITS,SUMMER_COLLECTIONS,WINTER_COLLECTIONS)
values(1,'Bot_zip','coat_suit','port_fabric','var_half','popcorn_fabric','curve_sleeve');
SELECT * FROM Clothzy_User_PROMOTION;
DROP TABLE CLOTHZY_USER_PROMOTION;

create table Clothzy_User_INTERESTED(
SNO int not null,
PRICE_RANGE varchar(255),
SHIRT_TYPE varchar(255),
BOTTOM_TYPE varchar(255),
OFFER_TYPE varchar(255),
BRAND_TYPE varchar(255)
);
DROP TABLE CLOTHZY_USER_INTERESTED;
insert into CLOTHZY_USER_INTERESTED(SNO,PRICE_RANGE,SHIRT_TYPE,BOTTOM_TYPE,OFFER_TYPE,BRAND_TYPE)
VALUES(1,'599-3499','Small','small','Membership_20%','Cltohzy_fashion'),(2,'599-3499','Medium','Medium','Membership_20%','Cltohzy_fashion'),
(3,'599-3499','Large','Large','Membership_20%','Cltohzy_fashion'),(4,'599-3499','X-Large','X-Large','Membership_20%','Cltohzy_fashion'),
(5,'599-3499','2X-Large','2X-Large','Membership_20%','Cltohzy_fashion'),(6,'599-3499','3X-Large','3X-Large','Membership_20%','Cltohzy_fashion'),
(7,'599-3499','34','34','Membership_20%','Cltohzy_fashion'),(8,'599-3499','36','36','Membership_20%','Cltohzy_fashion'),
(9,'599-3499','38','38','Membership_20%','Cltohzy_fashion'),(10,'599-3499','40','40','Membership_20%','Cltohzy_fashion'),
(11,'599-3499','42','42','Membership_20%','Cltohzy_fashion'),(12,'599-3499','44','44','Membership_20%','Cltohzy_fashion'),
(13,'599-3499','46','46','Membership_20%','Cltohzy_fashion');
select * from CLOTHZY_USER_INTERESTED;

CREATE TABLE  CLOTHZY_USER_PRODUCT_LIST(
VINTAGE_COLLECTIONS_QUANTITY long,
WEDDING_COLLECTIONS long,
FORMAL_OUTFITS long,
SEMIFORMAL_OUTFITS long,
SUMMER_COLLECTIONS long,
WINTER_COLLECTIONS long
);
SELECT * FROM CLOTHZY_USER_PRODUCT_LIST;
insert into  CLOTHZY_USER_PRODUCT_LIST(VINTAGE_COLLECTIONS_QUANTITY,WEDDING_COLLECTIONS,FORMAL_OUTFITS,
 WINTER_COLLECTIONS,SEMIFORMAL_OUTFITS,SUMMER_COLLECTIONS)values(500,250,600,400,300,400);
DROP table clothzy_user_product_LIST;



use cad_clothzy;
show tables;
select * from clothzy_user_reg;
delimiter $$
 create procedure insertvalue(
 IN SNOparam int ,
 in USER_IDparam int , 
 in FIRST_NAMEparam varchar(255) , 
 in LAST_NAMEparam varchar(255) ,
 in USER_NAMEparam varchar(255) , 
 in GENDERparam varchar(255) , 
 in AGEparam mediumtext, 
 in EMAILparam varchar(225) , 
 in CONTACT_NOparam long, 
 in ADDRESSparam varchar(255)
)
begin
insert into clothzy_user_reg(SNO,USER_ID,FIRST_NAME,LAST_NAME,USER_NAME,GENDER,AGE,EMAIL,CONTACT_NO,ADDRESS)
VALUES(SNOparam,USER_IDparam,FIRST_NAMEparam,LAST_NAMEparam,USER_NAMEparam,GENDERparam,AGEparam,EMAILparam,CONTACT_NOparam,ADDRESSparam);
END $$
delimiter ;

call insertvalue (1,101,'AARIF','S','@aarif01','MALE',25,'aarif01cad@gmail.com',9025171297,'MADURAI');
select * from clothzy_user_reg;


DELIMITER $$

drop procedure if exists updateValue; $$
create procedure updateValue(
in tablename varchar(50),
in columnname varchar(50),
in columnModifyValue varchar(50),
in conditionColumnName varchar(50),
in conditionCheckValue int 
)
begin

set @updatestatement =concat(' update ',tablename,' set ',columnname,'=\'',columnModifyValue, '\' where ' ,conditionColumnName,'=',conditionCheckValue);
prepare stmt from @updatestatement;
execute stmt;
set @selectstmt=concat('select * from ',tablename);
prepare stmt1 from @selectstmt;
execute stmt1;
end $$
delimiter ;

call updatevalue('clothzy_user_login','user_name','@abdul02','login_id',2);
 drop procedure updateValue;
 SELECT * FROM CLOTHZY_USER_LOGIN;

DELIMITER $$
DROP procedure IF exists altervalue; $$
create procedure altervalue(
in tablename varchar(50),
in columnname varchar(50),
in datatype varchar(50)
)
begin
set @altertstmt=concat('alter table ',tablename,' add ', columnname,' ', datatype);
prepare  SMT from @altertstmt;
execute SMT;
end $$ 
delimiter ;

call altervalue('clothzy_user_product_list', 'CLOTHZY_COLLECTIONS','VARCHAR(50)');
 DROP PROCEDURE altervalue;

select * from clothzy_user_product_list;