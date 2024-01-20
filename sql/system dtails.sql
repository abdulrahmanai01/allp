use ai_abdulrahman;
create table system_details
(
S_no int not null primary key auto_increment,
Name varchar(30) not null,
System_no int not null,
error_ varchar(50),
OS_Name varchar(100),
RAM varchar(30),
PROCESSOR varchar(100),
Mouse_Condition varchar(50),
Keyboard_Condition varchar (50),
foreign key (S_no) references ai_students_list (S_no)
);
select* from system_details;
insert into system_details(S_no,Name,System_no,error_,OS_name,RAM,PROCESSOR,Mouse_Condition,Keyboard_Condition) values 
(1,'Abdul Rahman  B',42,'working','windows 8.1 pro','2 Gb','Intel Pentium','working','workimg'),
(2,'Arun T',43,'working','windows 8.1','2.00GB','Intel Core 2 Duo','working','working'),
(3,'Aysha sithika L',17,'WORKING','windows 10 pro','2GB','INTEL CORE i3','working','working'),
(4,'Bhavani R',8,'working','windows 10 pro','4.00 GB','Intel Core i3','working','working'),
(5,'Fathima M',4,'visual C++ 2019','windows 7 ultimate ','2.00GB','Intel Core  i3','working','working'),
(6,'Ghouse bi S',18,'working','Windows 8.1 Pro','4GB','INTEL CORE i3',' working','working'),
(7,'Gnanagowsalya K',14,'working','windows 10 ProN','8.00 GB','INTEL CORE i5','working','working'),
(8,'Hajeera Sithika L',16,'working','windows 8.1','2GB','Intel Core 2 Duo','working','working'),
(9,'HARIHARAN A',38,'working','windows 8.1 pro','4.00 GB','INTEL CORE i3','working','working'),
(10,'Jayalakshmi R',3,'working','windows 8.1 pro','4.00 GB','INTEL CORE i3','working','working'),
(11,'Jothika J',15,'working','Windows 8.1 Pro','4.00 GB','INTEL CORE i3','working','working'),
(12,'Kalaiarasan A',32,'working','Windows 8.1 Pro','4.00 GB','INTEL CORE i3','working','working'),
(13,'Kayalvizhi M',1,'visual C++2019','Windows 7 Ultimate','4.00 GB','INTEL CORE i3','Working','working'),
(14,'Komaladevi. S',7,'visualc++2019','Windows 8.1 Pro','4.00  GB','Intel Pentium','Working','Working'),
(15,'LAVANYA M ',5,'visual C++ 2019','Windows 7 Ultimate','4.00 GB','Intel Core i3','Working','Working'),
(16,'Narayanan S',19,'Working','windows 8.1','4.00GB','INTEL CORE i3','working','working'),
(17,'Prasanth P',35,'C++2019','Windows 10 Pro','2.00 GB','Intel Pentium','Working','working'),
(18,'Priya S',23,'not  support by this processer tryp','windows 7 proffessional','4.00GP','INTEL CORE i3','working','working'),
(19,'Punithavathi D',9,'visual C++ 2019','windows 8.1 pro','2.00 GB','Intel Core 2 Duo','working','working'),
(20,'Raghul S',39,'not supported by the processor','windows 7','2.00 GB','Intel Pentium','Working','working'),
(21,'Roobankumar  K',34,'processor not supported','windows 7 ultimate','2.00GB','intel core 2 duo','working','working'),
(22,'Sangari S',2,'Working','windows 8.1 pro','2.00 GB','INTEL Pentium','working','Working'),
(23,'Santhiya S',13,'not supported by this processor type','windows 10 pro','4.00 GB','Intel Core 2 Duo','working','Working'),
(24,'Saranya N',6,'not supported by this processor type','Windows 7 Professional','2.00 GB','INTEL CORE i3','Working','Working'),
(25,'Saravanan M',37,'Working','Windows 8.1 Pro','4.00 GB','INTEL CORE i3','Working','Working'),
(26,'Snega D',10,'working','windows 10 pro','4.00 GB','intel core i3','working','working'),
(27,'Srinidhi S',12,'visual C++2019','windows 8.1','2.00 GB','INTEL CORE i3','working','working'),
(28,'Tamil V',11,'visual C++2019','windows 8.1','4.00 GB','INTEL CORE i3','working','working'),
(29,'Vinu Andrews S',33,'working','windows 8.1','2gb','Intel Core 2 Duo',' working','working'),
(30,'Yogarajan K',36,'Not supported by the processor','windows 10 pro','2 GB RAM ','Intel Pentium','working','working');

select* from ai_students_list n1 left join system_details n2 on n1.S_no=n2.S_no ;