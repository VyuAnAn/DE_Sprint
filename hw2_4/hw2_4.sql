-- Попробуйте вывести не просто самую высокую зарплату во всей команде, а вывести именно фамилию сотрудника с самой высокой зарплатой.		  
  select e.salary, e.last_name from public.employee e
  where e.salary = (select max(ee.salary)from public.employee ee);
-- Попробуйте вывести фамилии сотрудников в алфавитном порядке
  select e.last_name from public.employee e
  order by e.last_name;
-- Рассчитайте средний стаж для каждого уровня сотрудников  
select e.level,  
	   avg(age(timestamp '2022-11-14', e.start_data))
from public.employee e
group by e.level
-- Выведите фамилию сотрудника и название отдела, в котором он работает
select e.last_name, b.name
from public.employee e join public.branch b
on e.id_branch = b.id
--Выведите название отдела и фамилию сотрудника с самой высокой зарплатой в данном отделе и саму зарплату также.
select e.last_name, b.name
from public.employee e join public.branch b
on e.id_branch = b.id
where e.salary = (select max(ee.salary)from public.employee ee where ee.id_branch = b.id)
