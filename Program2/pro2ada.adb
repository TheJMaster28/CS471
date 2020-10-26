-- Jeffrey Lansford
-- 9/9/2020
-- Program 2
-- Ada program to test the short circut implementation of Ada
with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;

procedure Pro2ada is 
    A : Integer;
    -- function to see if it is executed during short circut evaluation
    function B return Integer is
    begin
        Put_Line("      Within B");
        return 1;
    end B;
begin

    Put_Line("A is always False and B is always True");
    
    Put_Line("Here are the two conditions with 'and'");
    A := 0;
    -- Do Short Circut Evaluation and 'and' statment in Ada
    -- A will evaluate to false and B will evalute to true
    Put_Line("A && B");
    if A = 1 and B = 1 then
        Put_Line("True");
    else 
        Put_Line("False");
    end if;

    -- B will evaluate to false and A will evalute to true
    Put_Line("B && A");
    if B = 1 and A = 1 then
        Put_Line("True");
    else 
        Put_Line("False");
    end if;

    -- Do Short Circut Evaluation and 'and then' statment in Ada
    Put_Line("");
    Put_Line("Here are the two conditions with 'and then' with short circuting");
    Put_Line("A && B");
    if A = 1 and then B = 1 then
        Put_Line("True");
    else 
        Put_Line("False");
    end if;

    -- B will evaluate to false and A will evalute to true
    Put_Line("B && A");
    if B = 1 and then A = 1 then
        Put_Line("True");
    else 
        Put_Line("False");
    end if;


end Pro2ada;


