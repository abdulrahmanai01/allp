use ai_abdulrahman;
create table stored_program
(name varchar(10) not null primary key,
age int,
wight int,
gender varchar(5));
select* from stored_program;
describe stored_program;

delimiter %%
drop procedure updatevalue; %%
create procedure updatevalue(in s_noparam int, in nameparam varchar(10), in ageparam int)
begin
update stored_program set name=nameparam,age=ageparam where s_no=s_noparam;
end %%
delimiter %%
call updatevalue(1,'ar007',23);
                                                                                                           