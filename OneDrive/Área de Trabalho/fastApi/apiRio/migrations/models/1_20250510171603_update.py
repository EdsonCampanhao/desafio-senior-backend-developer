from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `bilheteunico` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `amount` DECIMAL(10,2) NOT NULL,
    `user_id` INT NOT NULL,
    CONSTRAINT `fk_bilheteu_user_44377697` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
        CREATE TABLE IF NOT EXISTS `documents` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `issuingBody` VARCHAR(255) NOT NULL,
    `dateOfIssue` DATE NOT NULL,
    `registrationNumber` INT NOT NULL,
    `typeOfDocument_id` INT NOT NULL,
    `user_id` INT NOT NULL,
    CONSTRAINT `fk_document_typeofdo_7f39d77f` FOREIGN KEY (`typeOfDocument_id`) REFERENCES `typeofdocuments` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_document_user_93f97282` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
        CREATE TABLE IF NOT EXISTS `typeofdocuments` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4;
        CREATE TABLE IF NOT EXISTS `user` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL UNIQUE,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `password` LONGBLOB NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `bilheteunico`;
        DROP TABLE IF EXISTS `user`;
        DROP TABLE IF EXISTS `typeofdocuments`;
        DROP TABLE IF EXISTS `documents`;"""
