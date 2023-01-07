select ROUND(AVG(grade), 2), student_name
from graduates as g
left join students as s on g.student_id = s.id
group BY student_name
order by ROUND(AVG(grade), 2) desc 
limit 5




