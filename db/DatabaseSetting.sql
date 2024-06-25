/* 환율 테이블 생성 */
CREATE TABLE IF NOT EXISTS `exchange_rate` (
	`날짜` DATE NOT NULL,
	`환율` FLOAT NOT NULL,
	PRIMARY KEY (`날짜`)
)
COLLATE='utf8mb4_general_ci'
;

