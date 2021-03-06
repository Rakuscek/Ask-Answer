BEGIN;
--
-- Create model Answer
--
CREATE TABLE "AA_answer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "body" varchar(1000) NOT NULL, "time" datetime NOT NULL, "plusVotes" integer NOT NULL, "minusVotes" integer NOT NULL);
--
-- Create model Question
--
CREATE TABLE "AA_question" ("questionID" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "body" varchar(1000) NOT NULL, "time" datetime NOT NULL, "categories" varchar(500) NOT NULL, "answered" integer NOT NULL, "username_id" integer NULL REFERENCES "auth_user" ("id"));
--
-- Add field questionID to answer
--
ALTER TABLE "AA_answer" RENAME TO "AA_answer__old";
CREATE TABLE "AA_answer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "body" varchar(1000) NOT NULL, "time" datetime NOT NULL, "plusVotes" integer NOT NULL, "minusVotes" integer NOT NULL, "questionID_id" integer NOT NULL REFERENCES "AA_question" ("questionID"));
INSERT INTO "AA_answer" ("time", "minusVotes", "questionID_id", "body", "plusVotes", "id") SELECT "time", "minusVotes", NULL, "body", "plusVotes", "id" FROM "AA_answer__old";
DROP TABLE "AA_answer__old";
CREATE INDEX "AA_question_bbe0c9aa" ON "AA_question" ("username_id");
CREATE INDEX "AA_answer_ed8214f5" ON "AA_answer" ("questionID_id");
--
-- Add field username to answer
--
ALTER TABLE "AA_answer" RENAME TO "AA_answer__old";
CREATE TABLE "AA_answer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "body" varchar(1000) NOT NULL, "time" datetime NOT NULL, "plusVotes" integer NOT NULL, "minusVotes" integer NOT NULL, "questionID_id" integer NOT NULL REFERENCES "AA_question" ("questionID"), "username_id" integer NULL REFERENCES "auth_user" ("id"));
INSERT INTO "AA_answer" ("time", "minusVotes", "questionID_id", "body", "plusVotes", "username_id", "id") SELECT "time", "minusVotes", "questionID_id", "body", "plusVotes", NULL, "id" FROM "AA_answer__old";
DROP TABLE "AA_answer__old";
CREATE INDEX "AA_answer_ed8214f5" ON "AA_answer" ("questionID_id");
CREATE INDEX "AA_answer_bbe0c9aa" ON "AA_answer" ("username_id");
COMMIT;
