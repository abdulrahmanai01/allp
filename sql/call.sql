use ai_abdulrahman;
delimiter %%
create procedure ar007()
begin
select * from abdul_data;
end %%
delimiter ;
call ar007();
