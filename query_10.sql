select student_name, leson_name, profesor_name
from graduates as g
left join students as s on g.student_id = s.id
left join lesons as l on g.leson_id = l.id
left join groups as gr on s.group_id = gr.id
left join professors as p on l.id_profesor = p.id
where s.id = 3 and p.id = 2
group by leson_name



