 create table complaint (
    id int auto_increment primary key,
    name varchar(100),
    room int,
    hostel varchar(100),
    floor int,
    block varchar(50),
    complaint text,
    email varchar(100),
    status varchar(20) default 'Pending',
    created_at datetime default current_timestamp,
    updated_at datetime default current_timestamp on update current_timestamp
);
