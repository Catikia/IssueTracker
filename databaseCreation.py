#Created by: Catikia

import sqlite3 #needed for python to talk to SQLite

#Database for Issue Tracking Program
#by: Catherine Ackerson
#made for SQL Lite

#---------------- Start of Table creation -------------------------------------


#connects to or creates database if not there
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates table
cursor1.execute("""CREATE TABLE if not exists many_depts (
    department_id integer NOT NULL PRIMARY KEY,
    department_name text
    )"""
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates table
cursor1.execute("""CREATE TABLE if not exists managers_exist (
    manager_id integer NOT NULL PRIMARY KEY,
    first_name text,
    last_name text,
    department_id integer,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
    )"""
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates table
cursor1.execute("""CREATE TABLE if not exists people_work_here (
    employee_id integer NOT NULL PRIMARY KEY,
    first_name text,
    last_name text,
    department_id integer,
    manager_id integer,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id),
    FOREIGN KEY (manager_id)
        REFERENCES managers(manager_id)
    )"""
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates table
cursor1.execute("""CREATE TABLE if not exists progress_types (
    progress_id integer NOT NULL PRIMARY KEY,
    progress_level integer,
    progress_title text,
    progress_description text
    )"""
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates table
cursor1.execute("""CREATE TABLE if not exists dev_stages (
    dev_id integer NOT NULL PRIMARY KEY,
    dev_stage_name text
    )"""
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates table
cursor1.execute("""CREATE TABLE if not exists how_severe (
    severity_id integer NOT NULL PRIMARY KEY,
    severity_level integer,
    severity_title text,
    severity_description text
    )"""
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates table
cursor1.execute("""CREATE TABLE if not exists what_issues (
    issue_id integer NOT NULL PRIMARY KEY,
    issue_name text,
    issue_description text,
    reproduction_details text,
    other_details blob,
    dev_id integer,
    severity_id integer,
    deadline_date date,
    deadline_time time,
    management_priority integer,
    FOREIGN KEY (dev_id)
        REFERENCES development_stages(dev_id),
    FOREIGN KEY (severity_id)
        REFERENCES severity_levels(severity_id)
    )"""
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates table
cursor1.execute("""CREATE TABLE if not exists many_updates (
    status_id integer NOT NULL PRIMARY KEY,
    employee_id integer,
    issues_id integer,
    update_date date,
    update_time time,
    progress_id integer,
    status_comments text,
    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id),
    FOREIGN KEY (issues_id)
        REFERENCES issues(issues_id),
    FOREIGN KEY (progress_id)
        REFERENCES progress_levels(progress_id)
    )"""
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates table
cursor1.execute("""CREATE TABLE if not exists people_assigned (
    assigned_id integer NOT NULL PRIMARY KEY,
    issues_id integer,
    employee_id integer,
    date_assigned date,
    time_assigned time,
    FOREIGN KEY (issues_id)
        REFERENCES issues(issues_id),
    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
    )"""
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#------------------- Start of simple views creation ---------------------------
#--- for inserting, updating, and deleting data ---

#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates view
cursor1.execute("""CREATE VIEW if not exists [departments] as
    SELECT department_name
    FROM many_depts
    """
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates view
cursor1.execute("""CREATE VIEW if not exists [employees] as
    SELECT first_name, last_name
    FROM people_work_here
    """
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates view
cursor1.execute("""CREATE VIEW if not exists [managers] as
    SELECT first_name, last_name
    FROM managers_exist
    """
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates view
cursor1.execute("""CREATE VIEW if not exists [assigned] as
    SELECT date_assigned, time_assigned
    FROM people_assigned
    """
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates view
cursor1.execute("""CREATE VIEW if not exists [status_updates] as
    SELECT update_date, update_time, status_comments
    FROM many_updates
    """
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates view
cursor1.execute("""CREATE VIEW if not exists [issues] as
    SELECT issue_name, issue_description, reproduction_details, other_details,
     deadline_date, deadline_time, management_priority
    FROM what_issues
    """
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates view
cursor1.execute("""CREATE VIEW if not exists [severity_levels] as
    SELECT severity_level, severity_title, severity_description
    FROM how_severe
    """
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates view
cursor1.execute("""CREATE VIEW if not exists [development_stages] as
    SELECT dev_stage_name
    FROM dev_stages
    """
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates view
cursor1.execute("""CREATE VIEW if not exists [progress_levels] as
    SELECT progress_level, progress_title, progress_description
    FROM progress_types
    """
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#------------------ Start of complex view creation ----------------------------
#--- for queries/reports ---


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates view
#full joins are not supported in sqlite
cursor1.execute("""CREATE VIEW if not exists [who_works_where] as
    SELECT *
    FROM many_departments
    LEFT JOIN people_work_here
    ON many_departments.department_id = people_work_here.department_id
    UNION ALL
    SELECT *
    FROM people_work_here
    LEFT JOIN many_departments
    ON many_departments.department_id = people_work_here.department_id
    """
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()


#connects to database
conn = sqlite3.connect('issues.db')

#create cursor
cursor1 = conn.cursor()
#creates view
#full joins are not supported in sqlite
cursor1.execute("""CREATE VIEW if not exists [who_works_where] as
    SELECT *
    FROM many_departments
    LEFT JOIN people_work_here
    ON many_departments.department_id = people_work_here.department_id
    UNION ALL
    SELECT *
    FROM people_work_here
    LEFT JOIN many_departments
    ON many_departments.department_id = people_work_here.department_id
    """
)
#commits above commands to database
conn.commit()

#close connection to Database
conn.close()
