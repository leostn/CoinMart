drop table if exists users;
create table users(
  username text primary key,
  email text not null,
  password text not null

);
insert into users values('zozo', 'Zozo@gmail.com','1234Zozo');
insert into users values('admin', 'admin@gmail.com','Admin123');


