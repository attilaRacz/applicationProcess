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


@database_common.connection_handler
def applicants(cursor):
    cursor.execute("""SELECT first_name, application_code, creation_date
                      FROM applicants JOIN applicants_mentors
                      ON applicants.id = applicants_mentors.applicant_id
                      WHERE creation_date > '2016-01-01'::date
                      ORDER BY creation_date DESC;""")
    table = cursor.fetchall()
    headers = ["first_name", "application_code", "creation_date"]
    front_page = False
    return render_template("list.html", table=table, headers=headers, front_page=front_page)


@database_common.connection_handler
def applicants_and_mentors(cursor):
    cursor.execute("""SELECT applicants.first_name AS applicant_name, application_code,
                      COALESCE(mentors.first_name, 'No data') AS mentor_first_name,
                      COALESCE(mentors.last_name, 'No data') AS mentor_last_name
                      FROM applicants
                      LEFT JOIN applicants_mentors
                      ON applicants.id = applicants_mentors.applicant_id
                      LEFT JOIN mentors
                      ON applicants_mentors.mentor_id = mentors.id
                      ORDER BY applicants.id;""")
    table = cursor.fetchall()
    headers = ["applicant_name", "application_code", "mentor_first_name", "mentor_last_name"]
    front_page = False
    return render_template("list.html", table=table, headers=headers, front_page=front_page)
