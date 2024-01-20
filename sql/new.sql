use ai_abdulrahman;
create table abu_zon
(user_id int not null primary key auto_increment,
f_name varchar(200)  not null,
m_name varchar(50),
l_name varchar(50),
dob date,
phone_no long,
user_name varchar(10) not null unique,
password varchar(18) not null);
show tables;
select * from abu_zon;
insert into abu_zon(user_id,f_name,m_name,l_name,dob,phone_no,user_name,password)values(1,'abdul','rahman','basha','2001-01-15',9952630126,'rahman143','Ar007@123');
insert into abu_zon(user_id,f_name,m_name,l_name,dob,phone_no,user_name,password)values(2,'arun','rathi','tamil','2002-07-07',8525880306,'aruntamil','09876654321');
insert into abu_zon(user_id,f_name,m_name,l_name,dob,phone_no,user_name,password)values(3,'raghul','ji','anbu','2000-06-07',7070107069,'RAGHULJI','864387536');
