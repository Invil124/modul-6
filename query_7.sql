select grade, student_name, group_name, leson_name
from graduates as g
left join students as s on g.student_id = s.id
left join lesons as l on g.leson_id = l.id
left join groups as gr on s.group_id = gr.id
where gr.id = 1 and l.id = 3
order by student_name
