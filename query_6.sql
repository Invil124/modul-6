select student_name, group_name
from students as s
left join groups as gp on s.group_id = gp.id
where gp.id = 3
--- або можна group_name = "Group C"

