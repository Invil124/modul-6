select leson_name, profesor_name
from lesons as l
left join professors as p on l.id_profesor = p.id
where p.id = 2