select ROUND(AVG(grade), 2), student_name, leson_name
from graduates as g
left join students as s on g.student_id = s.id
left join lesons as l on g.leson_id = l.id
where leson_name = "History"
group BY student_name
order by ROUND(AVG(grade), 2) desc
limit 1
