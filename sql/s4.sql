use ai_abdulrahman;
delimiter %%
drop procedure if exists updatealltable;%%
create procedure updatealltable(in tablename varchar(30),
 in columnname varchar (40),
 in columnupdatevalue varchar (90),
 in conditioncolumnname varchar(98),
 in conditioncolumnvalue int )
 begin
 
 
 set @statement =concat("update ",tablename," set ",columnname,"=\'",columnupdatevalue,"\ ' where ",conditioncolumnname,"=",conditioncolumnvalue);
 prepare stmts from @statement;
 execute stmts;
 end %%
 delimiter ;
 
 