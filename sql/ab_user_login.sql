use ai_abdulrahman
select * from abu_zon;
create table ab_user_login (login_id 
insert into ab_user_login(login_id,user_name,password,new_password,user_id)values(110,'aruntamil','9988667329','Arun0087',2);
insert into ab_user_login(login_id,user_name,password,new_password,user_id)values(120,'RAGHULJI','9988667329','Arun0087',3);
select * from ab_user_login
insert into ab_user_login(login_id,user_name,password,new_password,user_id)values(130,'naveenktm','88489878','kolaru',4);
insert into ab_user_login(login_id,user_name,password,new_password,user_id)values(140,'handhari','77778557','kolaruD',5);



select * from abu_zon a1 left join ab_user_login a2 on a1.user_id=a2.user_id;


delimiter