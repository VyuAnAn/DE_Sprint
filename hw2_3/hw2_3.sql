-- Уникальный номер сотрудника, его ФИО и стаж работы – для всех сотрудников компании
select e.id, e.Last_name, e.first_name, e.middle_name, age(timestamp '2022-11-14', e.start_data) from public.employee e;
-- Уникальный номер сотрудника, его ФИО и стаж работы – только первых 3-х сотрудников
select e.id, e.Last_name, e.first_name, e.middle_name, age(timestamp '2022-11-14', e.start_data) 
  from public.employee e
  order by id limit 3;
-- Уникальный номер сотрудников - водителей  
select distinct e.id from public.employee e
  where lower(e.position) = 'водитель';
-- Выведите номера сотрудников, которые хотя бы за 1 квартал получили оценку D или E  
  select e.id from public.employee e
  where exists (select m.id from public.mark m where m.mark in ('D', 'E')
			  and m.id_employee = e.id);
-- Выведите самую высокую зарплату в компании.			  
  select max(e.salary) from public.employee e;
-- Выведите название самого крупного отдела
select b.name from public.branch b
where b.count_employees = (select max(bb.count_employees)from public.branch bb);
-- Выведите номера сотрудников от самых опытных до вновь прибывших
select e.id from public.employee e
order by age(timestamp '2022-11-14', e.start_data) desc;
-- Рассчитайте среднюю зарплату для каждого уровня сотрудников
select avg(e.salary), e.level from public.employee e
group by e.level;

