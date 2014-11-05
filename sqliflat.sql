BEGIN;
CREATE TABLE "django_flatpage_sites" (
    "id" integer NOT NULL PRIMARY KEY,
    "flatpage_id" integer NOT NULL,
    "site_id" integer NOT NULL REFERENCES "django_site" ("id"),
    UNIQUE ("flatpage_id", "site_id")
)
;
CREATE TABLE "django_flatpage" (
    "id" integer NOT NULL PRIMARY KEY,
    "url" varchar(100) NOT NULL,
    "title" varchar(200) NOT NULL,
    "content" text NOT NULL,
    "enable_comments" bool NOT NULL,
    "template_name" varchar(70) NOT NULL,
    "registration_required" bool NOT NULL
)
;
CREATE INDEX "django_flatpage_sites_872c4601" ON "django_flatpage_sites" ("flatpage_id");
CREATE INDEX "django_flatpage_sites_99732b5c" ON "django_flatpage_sites" ("site_id");
CREATE INDEX "django_flatpage_c379dc61" ON "django_flatpage" ("url");

COMMIT;
