from flask import Flask, render_template, request, redirect
import time
from datetime import datetime
import database_common

dt = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())


@database_common.connection_handler
def mentors_and_schools(cursor):
    cursor.execute("""SELECT first_name, last_name, name AS school_name, country
                      FROM mentors INNER JOIN schools
                      ON mentors.city = schools.city
                      ORDER BY mentors.id;""")
    table = cursor.fetchall()
    headers = ["first_name", "last_name", "school_name", "country"]
    front_page = False
    return render_template("list.html", table=table, headers=headers, front_page=front_page)


@database_common.connection_handler
def all_school(cursor):
    cursor.execute("""SELECT COALESCE(first_name, 'No data') AS first_name, COALESCE(last_name, 'No data') AS last_name,
                      name AS school_name, country
                      FROM mentors RIGHT JOIN schools
                      ON mentors.city = schools.city
                      ORDER BY mentors.id;""")
    table = cursor.fetchall()
    headers = ["first_name", "last_name", "school_name", "country"]
    front_page = False
    return render_template("list.html", table=table, headers=headers, front_page=front_page)


@database_common.connection_handler
def mentors_by_country(cursor):
    cursor.execute("""SELECT COUNT(*) AS counter, country
                      FROM mentors JOIN schools
                      ON mentors.city = schools.city
                      GROUP BY country
                      ORDER BY country;""")
    table = cursor.fetchall()
    headers = ["counter", "country"]
    front_page = False
    return render_template("list.html", table=table, headers=headers, front_page=front_page)


@database_common.connection_handler
def contacts(cursor):
    cursor.execute("""SELECT name AS school_name, first_name, last_name
                      FROM schools JOIN mentors
                      ON schools.contact_person = mentors.id;""")
    table = cursor.fetchall()
    headers = ["school_name", "first_name", "last_name"]
    front_page = False
    return render_template("list.html", table=table, headers=headers, front_page=front_page)

'''
Applicants page [/applicants]
On this page you should show the result of a query that returns the first name and
the code of the applicants plus the creation_date of the application
(joining with the applicants_mentors table) ordered by the creation_date in descending order
BUT only for applications later than 2016-01-01
columns: applicants.first_name, applicants.application_code, applicants_mentors.creation_date
'''
@database_common.connection_handler
def applicants(cursor):
    cursor.execute("""SELECT
                      FROM JOIN
                      ON
                      ORDER BY ;""")
    table = cursor.fetchall()
    headers = ["first_name", "last_name", "school_name", "country"]
    front_page = False
    return render_template("list.html", table=table, headers=headers, front_page=front_page)


@database_common.connection_handler
def applicants_and_mentors(cursor):
    cursor.execute("""SELECT
                      FROM JOIN
                      ON
                      ORDER BY ;""")
    table = cursor.fetchall()
    headers = ["first_name", "last_name", "school_name", "country"]
    front_page = False
    return render_template("list.html", table=table, headers=headers, front_page=front_page)
