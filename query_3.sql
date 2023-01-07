select ROUND(AVG(grade), 2), leson_name, group_name
from graduates as g
left join students as s on g.student_id = s.id
left join lesons as l on g.leson_id = l.id
left join groups as gr on s.group_id = gr.id
where leson_name = "Geography"
group BY group_name
order by ROUND(AVG(grade), 2) desc

