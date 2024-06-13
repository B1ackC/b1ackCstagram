use blackc;

CREATE TABLE TB_USERS(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    userId VARCHAR(255) NOT NULL,
    userPassword VARCHAR(255) NOT NULL,
    userName VARCHAR(255) NOT NULL,
);

CREATE TABLE TB_POSTS(
    postId INT NOT NULL AUTO_INCREMENT,
    postTitle VARCHAR(255) NOT NULL,
    postContent TEXT NOT NULL,
    postDate DATE NULL,
    userId INT NOT NULL,
    PRIMARY KEY(postId),
    FOREIGN KEY(userId) REFERENCES TB_USERS(id)
);