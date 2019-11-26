SELECT employees.emp_no,
employees.first_name,
employees.last_name,
employees.gender,
salaries.salary
From employees
inner join salaries on
salaries.emp_no = employees.emp_no

SELECT emp_no,
first_name,
last_name,
hire_date
FROM employees
WHERE hire_date > '12/31/1985' and hire_date < '01/01/1987'

SELECT 
d1.dept_no,
d1.dept_name,
d2.emp_no,
d3.last_name,
d3.first_name,
d2.from_date,
d2.to_date
FROM departments as d1
join dept_manager as d2 on
d1.dept_no = d2.dept_no
join employees as d3 on 
d2.emp_no = d3.emp_no;

SELECT
d3.emp_no,
d3.last_name,
d3.first_name,
d1.dept_name
FROM departments as d1
join dept_manager as d2 on
d1.dept_no = d2.dept_no
join employees as d3 on 
d2.emp_no = d3.emp_no;

SELECT 
employees.first_name,
employees.last_name
FROM employees
WHERE first_name = 'Hercules' 
and last_name like 'B%';

SELECT
d3.emp_no,
d3.last_name,
d3.first_name,
d1.dept_name
FROM departments as d1
join dept_manager as d2 on
d1.dept_no = d2.dept_no
join employees as d3 on 
d2.emp_no = d3.emp_no
Where d1.dept_name = 'Sales';

SELECT
d3.emp_no,
d3.last_name,
d3.first_name,
d1.dept_name
FROM departments as d1
join dept_manager as d2 on
d1.dept_no = d2.dept_no
join employees as d3 on 
d2.emp_no = d3.emp_no
Where d1.dept_name = 'Sales' or
d1.dept_name = 'Development';

SELECT
last_name, 
count(last_name) as cnt
FROM employees
group by last_name
order by cnt desc;



