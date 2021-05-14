#Created by: Catikia

import sqlite3 #needed for python to talk to SQLite

#Database for Issue Tracking Program
#by: Catherine Ackerson
#made for SQL Lite

#Add a new department record to departments table
def addDepartment(department_name):
    #connects to database
    conn = sqlite3.connect('issues.db')
    #create cursor
    cursor1 = conn.cursor()
    #adds department information
    cursor1.execute("INSERT INTO departments (department_name) VALUES (?)",
        (department_name,))
    #commits above commands to database
    conn.commit()
    #close connection to Database
    conn.close()

#Add a new manager record to managers table
def addManager(first_name, last_name, department_id):
    #connects to database
    conn = sqlite3.connect('issues.db')
    #create cursor
    cursor1 = conn.cursor()
    #adds manager information
    cursor1.execute("""INSERT INTO managers
        (first_name, last_name, department_id) VALUES (?, ?, ?)""",
        (first_name, last_name, department_id))
    #commits above commands to database
    conn.commit()
    #close connection to Database
    conn.close()

#Add a new employee record to employees table
def addEmployee(first_name, last_name, department_id, manager_id):
    #connects to database
    conn = sqlite3.connect('issues.db')
    #create cursor
    cursor1 = conn.cursor()
    #adds employee information
    cursor1.execute("""INSERT INTO employees
        (first_name, last_name, department_id, manager_id)
        VALUES (?, ?, ?, ?)""",
        (first_name, last_name, department_id, manager_id))
    #commits above commands to database
    conn.commit()
    #close connection to Database
    conn.close()

#add a new progress level record to the progress_levels table
def addProgressLevel(progress_level, progress_title, progress_description):
    #connects to database
    conn = sqlite3.connect('issues.db')
    #create cursor
    cursor1 = conn.cursor()
    #adds progress level information
    cursor1.execute("""INSERT INTO progress_levels
        (progress_level, progress_title, progress_description)
        VALUES (?, ?, ?)""",
        (progress_level, progress_title, progress_description))
    #commits above commands to database
    conn.commit()
    #close connection to Database
    conn.close()

#Add a new development stage record to development_stages table
def addDevStage(dev_stage_name):
    #connects to database
    conn = sqlite3.connect('issues.db')
    #create cursor
    cursor1 = conn.cursor()
    #adds development stage information
    cursor1.execute("INSERT INTO development_stages (dev_stage_name) VALUES (?)",
        (dev_stage_name,))
    #commits above commands to database
    conn.commit()
    #close connection to Database
    conn.close()

#add a new severity level record to the severity_levels table
def addSeverityLevel(severity_level, severity_title, severity_description):
    #connects to database
    conn = sqlite3.connect('issues.db')
    #create cursor
    cursor1 = conn.cursor()
    #adds severity level information
    cursor1.execute("""INSERT INTO severity_levels
        (severity_level, severity_title, severity_description)
        VALUES (?, ?, ?)""",
        (severity_level, severity_title, severity_description))
    #commits above commands to database
    conn.commit()
    #close connection to Database
    conn.close()

#add a new issue record to the issues table
def addIssue(issue_name, issue_description, reproduction_details,
    dev_id, severity_id, deadline_date, deadline_time, management_priority):
    #connects to database
    conn = sqlite3.connect('issues.db')
    #create cursor
    cursor1 = conn.cursor()
    #adds issue information
    cursor1.execute("""INSERT INTO issues
        (issue_name, issue_description, reproduction_details,
            dev_id, severity_id, deadline_date, deadline_time, management_priority)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (issue_name, issue_description, reproduction_details,
            dev_id, severity_id, deadline_date, deadline_time, management_priority))
    #commits above commands to database
    conn.commit()
    #close connection to Database
    conn.close()

#add a new status update record to the status_updates table
def addStatusUpdate(employee_id, issues_id, update_date,
    update_time, progress_id, status_comments):
    #connects to database
    conn = sqlite3.connect('issues.db')
    #create cursor
    cursor1 = conn.cursor()
    #adds status update information
    cursor1.execute("""INSERT INTO status_updates
        (employee_id, issues_id, update_date,
            update_time, progress_id, status_comments)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (employee_id, issues_id, update_date,
            update_time, progress_id, status_comments))
    #commits above commands to database
    conn.commit()
    #close connection to Database
    conn.close()

#add a new record assigning an issue to an employee on the Assigned table
def addAssignment(issues_id, employee_id, date_assigned, time_assigned):
        #connects to database
        conn = sqlite3.connect('issues.db')
        #create cursor
        cursor1 = conn.cursor()
        #adds assignment information
        cursor1.execute("""INSERT INTO assigned
            (issues_id, employee_id, date_assigned, time_assigned)
            VALUES (?, ?, ?, ?)""",
            (issues_id, employee_id, date_assigned, time_assigned))
        #commits above commands to database
        conn.commit()
        #close connection to Database
        conn.close()
