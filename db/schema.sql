drop table if exists entries;
create table entries (
    id      integer primary key autoincrement,
    title   string not null,
    text    string not null,
    created timestamp not null,
    type    integer not null,
    FOREIGN KEY(type) REFERENCES entry_type(id)
);

drop table if exists entry_type;
create table entry_type (
    id integer primary key autoincrement,
    type string not null
);

insert into entry_type values (0, "note");
insert into entry_type values (1, "blog");

insert into entries values (0,"Sample Entry", "This is an example entry", date("now"), 0 );


drop table if exists users;
create table users (
    id              integer primary key automincrement,
    first_name      string not null,
    last_name       string not null,
    user_name       string not null,
    password        string not null,
    is_admin           integer,
    pw_salt         string not null,
);

