CREATE TABLE `despesas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(100) NOT NULL,
  `valor` float NOT NULL,
  `data_despesa` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `forma_pagamento` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci