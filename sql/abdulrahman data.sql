show databases;
create database ai_abdulrahman;
use ai_abdulrahman;
create table abdul_data(s_no int not null primary key, name varchar(20)not null, phone_no long,age int,location varchar(250));
show tables;
insert into abdul_data(s_no,name,phone_no,age,location) values (1,'Arun',8525880306,21,'keeranur');
insert into abdul_data(s_no,name,phone_no,age,location) values (2,'raghul',9876543210,23,'kattur');
insert into abdul_data(s_no,name,phone_no,age,location) values (3,'abdul',9876543211,21,'trichy');
insert into abdul_data(s_no,name,phone_no,age,location) values (4,'hari',9876543211,22,'perabalur');
select *from abdul_data; 
alter table abdul_data add column address varchar(200);
update abdul_data set address ='4\79 quaid e millth nagar ariyamangalam trichy 10' where name = 'abdul';
update abdul_data set address ='23/45 gandi nagar thendral st trichy 15' where name = 'Arun';
update abdul_data set address ='65/54 indra st gv nagar trichy 02' where name = 'hari';
update abdul_data set address ='99/87 ajith nagar ak st trichy 08' where name = 'raghul';
update abdul_data set age =
case s_no
when 1 then '22'
when 2 then '23'
when 3 then '22'
when 4 then '25'
end,
location=
case s_no 
when 1 then'keeranoor'
when 2 then 'oil mil'
when 3 then 'ambikaburam'
end;

