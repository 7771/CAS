drop database CASDB;
create database CASDB;
use CASDB;

create table child(
    cid int (25), not null primary key,
    f_name char (25) not null,
    l_name char (30) not null,
    m_name char(25) not null,
    d.o.b. date not null,
    guardian char (50) not null,
    nurse_comments (200),
    m_comments char(200),
    sex char (1) not null,
    illness char (100),
    phone int(10),
    email char (20),
    
    foreign key nurse_comment references nurse(nurse_comments) on update cascade on delete cascade,
    foreign key m_comment references worker(m_comments) on update cascade on delete cascade,
    foreign key gid references parent(pid) on update cascade on delete cascade,
    primary key (cid),
    constraint unique (cid)
)engine=innodb, auto_increment = 1;

create table event(
	event_id int(6) not null primary key auto_increment,
	event_name char(15),
	event_year date not dull
)engine=innodb, auto_increment = 1;

create table worker(
staff_id int(6) not null primary key,
wName char(30) not null,
location char(20) not null,
nurse boolean not null,
primary key (customer_id),
constraint unique (customer_id)
)engine=innodb, auto_increment = 1;

create table comments(
comment_id int(6) NOT NULL auto_increment ,
cDate date,
comment_content char(200) not null,
child int(10),
mentor int(10),
nurse int(10),
foreign key (cid) references child(customer_id) on update cascade on delete cascade,
foreign key (mentor) references worker(customer_id) on update cascade on delete cascade,
foreign key (nurse) references worker(customer_id) on update cascade on delete cascade,
primary key (loan_number),
constraint unique (loan_number)
)engine=innodb, auto_increment = 1;
