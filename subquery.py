select *
from employees
where salary<(
		select salary
		from employees
		where employee_id=144
);




