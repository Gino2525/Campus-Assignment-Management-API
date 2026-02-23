--
-- Create model Department
--
CREATE TABLE "assignments_department" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL UNIQUE);
--
-- Create model Student
--
CREATE TABLE "assignments_student" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "username" varchar(150) NOT NULL UNIQUE, "name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL UNIQUE, "password" varchar(255) NOT NULL, "year" integer NOT NULL, "created_at" datetime NOT NULL, "department_id" bigint NULL REFERENCES "assignments_department" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Assignment
--
CREATE TABLE "assignments_assignment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL UNIQUE, "description" text NOT NULL, "subject" varchar(100) NOT NULL, "status" varchar(20) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "student_id" bigint NOT NULL REFERENCES "assignments_student" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "assignments_student_department_id_09d21f01" ON "assignments_student" ("department_id");
CREATE INDEX "assignments_assignment_student_id_5a1f8791" ON "assignments_assignment" ("student_id");
COMMIT;