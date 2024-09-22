CREATE TABLE `encomendas` (
  `i_iddavenda` int NOT NULL AUTO_INCREMENT,
  `s_nomedocliente` varchar(50) DEFAULT NULL,
  `i_quantidade` int NOT NULL,
  `s_nomedoproduto` varchar(50) NOT NULL,
  `f_valordoproduto` float NOT NULL,
  `s_promocao` varchar(20) NOT NULL,
  `s_formadepagamento` varchar(20) NOT NULL,
  `d_datadavenda` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `s_tipodeentrega` varchar(50) NOT NULL,
  PRIMARY KEY (`i_iddavenda`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci