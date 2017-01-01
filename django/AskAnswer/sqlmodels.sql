BEGIN;
--
-- Create model Answer
--
CREATE TABLE "home_answer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "body" varchar(1000) NOT NULL, "time" datetime NOT NULL);
--
-- Create model Question
--
CREATE TABLE "home_question" ("questionID" integer NOT NULL PRIMARY KEY, "title" varchar(200) NOT NULL, "body" varchar(1000) NOT NULL, "plusVotes" integer NOT NULL, "minusVotes" integer NOT NULL, "time" datetime NOT NULL, "categories" varchar(500) NOT NULL, "username_id" integer NULL REFERENCES "auth_user" ("id"));
--
-- Add field questionID to answer
--
ALTER TABLE "home_answer" RENAME TO "home_answer__old";
CREATE TABLE "home_answer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "body" varchar(1000) NOT NULL, "time" datetime NOT NULL, "questionID_id" integer NOT NULL REFERENCES "home_question" ("questionID"));
INSERT INTO "home_answer" ("id", "time", "body", "questionID_id") SELECT "id", "time", "body", NULL FROM "home_answer__old";
DROP TABLE "home_answer__old";
CREATE INDEX "home_question_bbe0c9aa" ON "home_question" ("username_id");
CREATE INDEX "home_answer_ed8214f5" ON "home_answer" ("questionID_id");
--
-- Add field username to answer
--
ALTER TABLE "home_answer" RENAME TO "home_answer__old";
CREATE TABLE "home_answer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "body" varchar(1000) NOT NULL, "time" datetime NOT NULL, "questionID_id" integer NOT NULL REFERENCES "home_question" ("questionID"), "username_id" integer NULL REFERENCES "auth_user" ("id"));
INSERT INTO "home_answer" ("id", "time", "body", "questionID_id", "username_id") SELECT "id", "time", "body", "questionID_id", NULL FROM "home_answer__old";
DROP TABLE "home_answer__old";
CREATE INDEX "home_answer_ed8214f5" ON "home_answer" ("questionID_id");
CREATE INDEX "home_answer_bbe0c9aa" ON "home_answer" ("username_id");
COMMIT;
