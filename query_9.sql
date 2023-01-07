select student_name, leson_name
from graduates as g
left join students as s on g.student_id = s.id
left join lesons as l on g.leson_id = l.id
left join groups as gr on s.group_id = gr.id
left join professors as p on l.id_profesor = p.id
where s.id = 3
---- also work s.student_name = "NAME OF STUDENT"
group by leson_name



