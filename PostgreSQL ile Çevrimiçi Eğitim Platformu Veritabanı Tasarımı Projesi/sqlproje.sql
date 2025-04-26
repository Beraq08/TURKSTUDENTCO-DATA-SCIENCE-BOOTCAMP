-- Kategoriler tablosu
CREATE TABLE categories (
    category_id SMALLINT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Üyeler tablosu
CREATE TABLE members (
    member_id BIGINT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Eğitimler tablosu
CREATE TABLE courses (
    course_id BIGINT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    instructor VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    category_id SMALLINT REFERENCES categories(category_id)
);

-- Katılımlar tablosu
CREATE TABLE enrollments (
    enrollment_id BIGINT PRIMARY KEY,
    member_id BIGINT NOT NULL REFERENCES members(member_id),
    course_id BIGINT NOT NULL REFERENCES courses(course_id),
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (member_id, course_id)
);

-- Sertifikalar tablosu
CREATE TABLE certificates (
    certificate_id BIGINT PRIMARY KEY,
    certificate_code VARCHAR(100) NOT NULL UNIQUE,
    issue_date DATE NOT NULL,
    course_id BIGINT NOT NULL REFERENCES courses(course_id)
);

-- Sertifika Atamaları tablosu
CREATE TABLE certificate_assignments (
    assignment_id BIGINT PRIMARY KEY,
    member_id BIGINT NOT NULL REFERENCES members(member_id),
    certificate_id BIGINT NOT NULL REFERENCES certificates(certificate_id),
    assignment_date DATE DEFAULT CURRENT_DATE,
    UNIQUE (member_id, certificate_id)
);

-- Blog Gönderileri tablosu
CREATE TABLE blog_posts (
    post_id BIGINT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    author_id BIGINT NOT NULL REFERENCES members(member_id),
    publication_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
