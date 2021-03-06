create table firstedge
(
	-- 15 relationships
	NODE_ID				INTEGER		not null primary key,
	NODE_LABEL			VARCHAR(32),
	HAS_CREATOR_ID		INTEGER,
	IS_LOCATED_IN_ID	INTEGER,
	REPLY_OF_ID			INTEGER,
	CONTAINER_OF_ID		INTEGER,
	HAS_MEMBER_ID		INTEGER,
	--forum_hasMember_person
	HAS_MEMBER_VALUE	DATE,
	HAS_MODERATOR_ID	INTEGER,
	HAS_TAG_ID			INTEGER,
	HAS_INTEREST_ID		INTEGER,	
	KNOWS_ID			INTEGER,
	--person_knows_person
	KNOWS_VALUE			DATE,
	LIKES_ID			INTEGER,
	--person_likes_comment
	--person_likes_post
	LIKES_VALUE			DATE,
	IS_PART_OF_ID		INTEGER,
	IS_SUBCLASS_OF_ID	INTEGER,
	HAS_TYPE_ID			INTEGER,
	STUDY_AT_ID			INTEGER,
	--person_studyAt_organisation
	STUDY_AT_VALUE		DATE,
	WORK_AT_ID			INTEGER,
	--person_workAt_organisation
	WORK_AT_VALUE		DATE
);

create table secondedge
(
	VALUEID			INTEGER not null,
	ENDNODEID		INTEGER,
	EDGEVALUE		DATE
);
-- alter table secondedge
-- 		add constraint fk_secondedge_id foreign key (VALUEID)
-- 				references firstedge ()

create table vertex
(
	NODE_ID			INTEGER	not null primary key,
	NODE_LABEL		VARCHAR(32),
	TYPE			VARCHAR(32),
	CREATION_DATE	DATE,
	FIRST_NAME		VARCHAR(100),
	LAST_NAME		VARCHAR(100),
	GENDER			VARCHAR(32),
	BIRTHDAY		DATE,
	EMAIL			VARCHAR(100),
	SPEAKS			VARCHAR(100),
	BROWSER_USED	VARCHAR(100),
	LOCATION_IP		VARCHAR(100),
	NAME			VARCHAR(100),
	CONTENT			VARCHAR(1024),
	LENGTH			INTEGER,
	ID				INTEGER,
	LANGUAGE		VARCHAR(100),
	IMAGE_FILE		VARCHAR(1024),
	TITLE			VARCHAR(256),
	URL				VARCHAR(1024)
)