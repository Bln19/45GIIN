-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-01-2024 a las 22:16:54
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inventarioberiestudio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `codigo_qr`
--

CREATE TABLE `codigo_qr` (
  `id_codigoqr` int(11) NOT NULL,
  `codigo_qr` text NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `imagen` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `codigo_qr`
--

INSERT INTO `codigo_qr` (`id_codigoqr`, `codigo_qr`, `estado`, `imagen`) VALUES
(6, '', 1, ''),
(7, '', 1, ''),
(8, '', 1, ''),
(9, '', 1, ''),
(10, '', 1, ''),
(11, '', 1, ''),
(12, '', 1, ''),
(13, '', 1, ''),
(14, '', 1, ''),
(15, '', 1, ''),
(16, '', 1, ''),
(17, '', 1, ''),
(18, '', 1, ''),
(19, '', 1, ''),
(20, '', 0, ''),
(28, 'D0300012MM47', 1, 'qrfolder\\qr_code_D0300012MM47.png'),
(29, 'ARONAC124CP', 1, 'qrfolder\\qr_code_ARONAC124CP.png'),
(30, 'ARONAC124CP', 1, 'qrfolder\\qr_code_ARONAC124CP.png'),
(31, 'ARONAC124CP', 1, 'qrfolder\\qr_code_ARONAC124CP.png'),
(32, 'ARONAC124CP', 1, 'qrfolder\\qr_code_ARONAC124CP.png'),
(33, 'ARONAC124CP', 1, 'qrfolder/qr_code_ARONAC124CP.png'),
(34, 'ARONAC124CP', 1, 'qrfolder/qr_code_ARONAC124CP.png'),
(35, 'Noa54630', 1, 'qrfolder/qr_code_Noa54630.png'),
(36, 'dasdasd', 1, 'qrfolder/qr_code_dasdasd.png'),
(37, '543aecaew', 1, 'qrfolder/qr_code_543aecaew.png'),
(38, '6847654', 1, 'qrfolder/qr_code_6847654.png'),
(39, 'kjañks2318', 1, 'qrfolder/qr_code_kjañks2318.png'),
(40, '4562464321', 1, 'qrfolder/qr_code_4562464321.png'),
(41, 'Noa5463055', 1, 'qrfolder/qr_code_Noa5463055.png'),
(42, 'KKK46546513', 1, 'qrfolder/qr_code_KKK46546513.png'),
(43, 'KKK465465123', 1, 'qrfolder/qr_code_KKK465465123.png'),
(44, 'KKK465465123', 1, 'qrfolder/qr_code_KKK465465123.png'),
(45, 'ARONAC124CP556rff', 1, 'qrfolder/qr_code_ARONAC124CP556rff.png'),
(46, 'D0300012MM47', 1, 'qrfolder/qr_code_D0300012MM47.png'),
(47, 'D0300012MM47ass', 1, 'qrfolder/qr_code_D0300012MM47ass.png'),
(48, 'D0300012MM47assH', 1, 'qrfolder/qr_code_D0300012MM47assH.png'),
(49, 'A1299-NEGR', 1, 'qrfolder/qr_code_A1299-NEGR.png'),
(50, 'N0500004MY12', 1, 'qrfolder/qr_code_N0500004MY12.png'),
(51, 'A680-004', 1, 'qrfolder/qr_code_A680-004.png'),
(52, 'A680-004', 1, 'qrfolder/qr_code_A680-004.png'),
(53, 'A680-004', 1, 'qrfolder/qr_code_A680-004.png'),
(54, 'A680-004', 1, 'qrfolder/qr_code_A680-004.png'),
(55, 'A680-004', 1, 'qrfolder/qr_code_A680-004.png'),
(56, '29591', 1, 'qrfolder/qr_code_29591.png'),
(57, '29591', 1, 'qrfolder/qr_code_29591.png'),
(58, '33717', 1, 'qrfolder/qr_code_33717.png'),
(59, '33717', 1, 'qrfolder/qr_code_33717.png'),
(60, '33529B', 1, 'qrfolder/qr_code_33529B.png'),
(61, 'PRUEBA54', 1, 'qrfolder/qr_code_PRUEBA54.png'),
(62, 'PRUEBA54', 1, 'qrfolder/qr_code_PRUEBA54.png'),
(63, 'dadq4578', 1, 'qrfolder/qr_code_dadq4578.png'),
(64, '465131jh', 1, 'qrfolder/qr_code_465131jh.png'),
(65, 'PRUEBA548', 1, 'qrfolder/qr_code_PRUEBA548.png'),
(66, 'A680-00458', 1, 'qrfolder/qr_code_A680-00458.png'),
(67, '124907-253996', 1, 'qrfolder/qr_code_124907-253996.png'),
(68, 'CC1720M40', 1, 'qrfolder/qr_code_CC1720M40.png'),
(69, 'CC1804PK81', 1, 'qrfolder/qr_code_CC1804PK81.png'),
(70, '6739226', 1, 'qrfolder/qr_code_6739226.png'),
(71, 'Ginger55', 1, 'qrfolder/qr_code_Ginger55.png'),
(72, 'Oto66R', 1, 'qrfolder/qr_code_Oto66R.png'),
(73, 'Silu180R', 1, 'qrfolder/qr_code_Silu180R.png'),
(74, '28081-0', 1, 'qrfolder/qr_code_28081-0.png'),
(75, '27001', 1, 'qrfolder/qr_code_27001.png'),
(76, '8-217606', 1, 'qrfolder/qr_code_8-217606.png'),
(77, 'CC2250FN46', 1, 'qrfolder/qr_code_CC2250FN46.png'),
(78, 'CC2250FN46', 1, 'qrfolder/qr_code_CC2250FN46.png'),
(79, 'CC2250FN46', 1, 'qrfolder/qr_code_CC2250FN46.png'),
(80, 'CC2250FN46', 1, 'qrfolder/qr_code_CC2250FN46.png'),
(81, '122121-246903', 1, 'qrfolder/qr_code_122121-246903.png'),
(82, '167038', 1, 'qrfolder/qr_code_167038.png'),
(83, '183658', 1, 'qrfolder/qr_code_183658.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresa`
--

CREATE TABLE `empresa` (
  `id_empresa` int(11) NOT NULL,
  `nombre` text NOT NULL,
  `direccion` text NOT NULL,
  `cif` varchar(9) NOT NULL,
  `email` text NOT NULL,
  `telefono` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empresa`
--

INSERT INTO `empresa` (`id_empresa`, `nombre`, `direccion`, `cif`, `email`, `telefono`) VALUES
(1, 'Beri Estudio Creativo S.L.U', 'Calle Convent, 15 Bajo Almenara (Castellon) 12590', 'B12934162', 'info@beriestudio.es', '+34962623687');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario`
--

CREATE TABLE `inventario` (
  `id_inventario` int(11) NOT NULL,
  `id_empresa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inventario`
--

INSERT INTO `inventario` (`id_inventario`, `id_empresa`) VALUES
(1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_producto`
--

CREATE TABLE `inventario_producto` (
  `id_inventario_producto` int(11) NOT NULL,
  `id_inventario` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inventario_producto`
--

INSERT INTO `inventario_producto` (`id_inventario_producto`, `id_inventario`, `id_producto`, `stock`) VALUES
(10, 1, 63, 16),
(12, 1, 71, 3),
(13, 1, 72, 1),
(14, 1, 73, 5),
(15, 1, 74, 3),
(16, 1, 75, 8),
(17, 1, 76, 0),
(18, 1, 77, 4),
(19, 1, 78, 3),
(20, 1, 79, 3),
(23, 1, 83, 1),
(24, 1, 84, 8),
(25, 1, 85, 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido`
--

CREATE TABLE `pedido` (
  `id_pedido` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedido`
--

INSERT INTO `pedido` (`id_pedido`, `fecha`, `estado`) VALUES
(14, '2024-01-14', 1),
(18, '2024-01-21', 1),
(19, '2024-01-21', 1),
(20, '2024-01-21', 0),
(21, '2024-01-22', 1),
(22, '2024-01-24', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido_producto`
--

CREATE TABLE `pedido_producto` (
  `id_pedido_producto` int(11) NOT NULL,
  `id_pedido` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedido_producto`
--

INSERT INTO `pedido_producto` (`id_pedido_producto`, `id_pedido`, `id_producto`, `cantidad`) VALUES
(15, 14, 63, 1),
(16, 14, 72, 1),
(22, 18, 83, 1),
(23, 18, 76, 1),
(24, 19, 74, 1),
(25, 19, 78, 1),
(26, 20, 73, 1),
(27, 20, 72, 1),
(28, 21, 83, 1),
(29, 21, 76, 1),
(30, 22, 83, 2),
(31, 22, 85, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id_producto` int(11) NOT NULL,
  `id_codigoqr` int(11) NOT NULL,
  `imagen` varchar(255) NOT NULL,
  `referencia` text NOT NULL,
  `nombre` text NOT NULL,
  `descripcion` text NOT NULL,
  `tamano` text NOT NULL,
  `color` text NOT NULL,
  `material` text NOT NULL,
  `precio` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id_producto`, `id_codigoqr`, `imagen`, `referencia`, `nombre`, `descripcion`, `tamano`, `color`, `material`, `precio`) VALUES
(63, 60, 'uploads/VicalMisha.JPG', '33529B', 'Mischa', 'Lámpara étnica de madera de abedul.', '82x60x82 cm', 'Natural', 'Madera de Abedul', 1056),
(71, 68, 'uploads/NadyriaKaveHome.JPG', 'CC1720M40', 'Nadyria', 'Mueble TV Nadyria 3 puertas chapa de roble y acero.', '180x43x50 cm', 'Natural y negro', 'Chapa de roble y acero', 825),
(72, 69, 'uploads/silla-mahalia-mostaza-y-patas-de-acero-acabado-pintado-negro.jpg', 'CC1804PK81', 'Mahalia', 'Silla Mahalia mostaza y patas de acero acabado pintado negro', '51x51x52cm', 'Mostaza', 'Tejido y acero', 109),
(73, 70, 'uploads/Marset_Djembe.JPG', '6739226', 'Djembé', 'lámpara colgante Djembé', '41.6 x 41.6 x 21 cm', 'Blanco', 'Polietileno', 914.76),
(74, 71, 'uploads/OndarretaGinger.JPG', 'Ginger55', 'Ginger', 'Mesa baja que se distingue por la curvatura de sus patas y sus formas redondeadas.', '55x45x34 cm', 'Natural', 'Roble', 673),
(75, 72, 'uploads/OndarretaOto.JPG', 'Oto66R', 'Oto', 'Taburete de cocina con estructura de madera y apoyo para pies.', '35 x 35 x 66 cm', 'Natural', 'Roble', 279.87),
(76, 73, 'uploads/OndarretaSilu.JPG', 'Silu180R', 'Silu', 'Mesa fabricada en madera maciza de roble.', '180x90x75 cm', 'Natural', 'Roble', 2727.95),
(77, 74, 'uploads/OleSento.JPG', '28081-0', 'Sento', 'Lámpara colgante de pantalla metálica de Ø31 cm en negro', '31x31x200 cm', 'Negro', 'Metal', 174.77),
(78, 75, 'uploads/OlePot.JPG', '27001', 'Pot', 'Sobremesa con una pantalla de Ø16 cm que permite una rotación de 140º.', '22 x 22 x 38.5 cm', 'Negro', 'Metal', 214),
(79, 76, 'uploads/IxiaSillonGris.JPG', '8-217606', 'SillonBeigeGris', 'Sillón moderno y elegante', '85 x 81 x 100 cm', 'Beige grisáceo', 'Tejido y Metal', 693),
(83, 80, '', 'CC2250FN46', 'Rexit', 'Armario de chapa y madera maciza de mindi, con tonalidades y vetas irrepetibles en cada pieza, con frontal de ratán trenzado.', '90 x 38 x 160 cm', 'Natural', 'Madera maciza de mindi y Ratán', 875),
(84, 81, 'uploads/SklumLali.JPG', '122121-246903', 'Lali', 'Silla de comedor en madera, tapizada y con reposabrazos', '52 x 54 x 79 cm', 'Natural', 'Madera, ratán tapizada', 155),
(85, 82, 'uploads/WestwingDream.JPG', '167038', 'Dream', 'Cama tapizada  con espacio de almacenamiento', '156 x 222 x 110 cm', 'Beige Lino', 'Poliester', 1049);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto_proveedor`
--

CREATE TABLE `producto_proveedor` (
  `id_producto_proveedor` int(11) NOT NULL,
  `id_proveedor` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto_proveedor`
--

INSERT INTO `producto_proveedor` (`id_producto_proveedor`, `id_proveedor`, `id_producto`) VALUES
(17, 1, 71),
(18, 1, 72),
(19, 37, 73),
(20, 10, 74),
(21, 10, 75),
(22, 10, 76),
(23, 5, 77),
(24, 5, 78),
(25, 2, 79),
(26, 3, 63),
(28, 1, 83),
(29, 45, 84),
(30, 46, 85);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE `proveedor` (
  `id_proveedor` int(11) NOT NULL,
  `nombre` text NOT NULL,
  `cif` varchar(9) NOT NULL,
  `direccion` text NOT NULL,
  `telefono` text NOT NULL,
  `email` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`id_proveedor`, `nombre`, `cif`, `direccion`, `telefono`, `email`) VALUES
(1, 'Julià Grup Furniture Solutions S.L', 'Carrer Ta', 'B45789873', 'info@juliagrup.es', '+34 972853628'),
(2, 'Ixia Regal', 'B83789526', 'Av. Juguete, 20, 03440 Ibi, Alicante', '+34965550615', 'pedidos@ixiaregal.es'),
(3, 'Vical Home', 'B78123456', 'Polígono industrial El carrascot, Avenida dels vidriers, 9, 46850 L\'Olleria, Valencia', ' +34962200060', 'info@vical.com'),
(4, 'Aromas del Campo', 'B12987123', 'Polígono Industrial L\'Horta Vella Calle 7 Parcela 3, 46117 Bétera, Valencia', '+34962737953', 'pedidos@aromasdelcampo.es'),
(5, 'Ole! Lighting', 'B34589678', 'Carrer Germanies, 14, 46960 Aldaia, Valencia', '+34961515977', 'info@ole-lighting.com'),
(6, 'La Ventana de Colores', 'B45789642', 'C. Juana Francés, 2, NAVE 6, 28522 Rivas-Vaciamadrid, Madrid', '+34914541800', 'info@LaVentanaDeColores.es'),
(7, 'Vive Mobiliario', 'B47895632', 'Carretera Rossell km 5\'4, 12511 Rossell, Castellón', '+34977575397', 'vive@vivemuebles.com'),
(8, 'Naxani', 'B45879311', 'Avinguda de la Llibertat, 38, 46600 Alzira, Valencia', '+34962456363', 'info@naxani.com'),
(9, 'Codis Bath', 'B47932765', 'Área Anardi Nº4A. 20730 Azpeitia (GIPUZKOA)', '+34943813007', 'info@codisbath.com'),
(10, 'Ondarreta', 'B89635671', 'Zuaznabar Kalea, 83.\r\n20180, Oiartzun, Gipuzkoa (España)', '+34943490301', 'hola@ondarreta.com'),
(11, 'Cifre', 'B15986432', 'Ctra. Vila-real-Onda, Km. 10\r\n12200 Onda, Castellón (Spain)', '+34964506969', 'pedidos@cifreceramica.com'),
(31, 'Thai Natura S.L.', 'B38897836', 'Calle virgen de los lirios, 12 - 03440 - Ibi (Alicante)', 'info@ilotinteriors.com', '+34902161617'),
(37, 'Marset Iluminacion S.A.', 'A08462681', 'Carretera de Rubí, 284, 08228 Terrassa, Barcelona', '934602067', 'info@marset.com'),
(45, 'Sklum', 'B98845936', 'Calle Partida Tancaes S/n 46720, Villalonga (Valencia)', '+34910210465', 'contacto@tikamoon.com'),
(46, 'Westwing', 'Av. Diago', 'B65732984', '+34 912 582 937', 'info@westwing.es'),
(49, 'Hannun S.A-', 'A67120683', 'Carrer de la Conca de Barberà, 18, 08211 Castellar del Vallès, Barcelona', '+34 932209473', 'tienda@hannun.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `codigo_qr`
--
ALTER TABLE `codigo_qr`
  ADD PRIMARY KEY (`id_codigoqr`);

--
-- Indices de la tabla `empresa`
--
ALTER TABLE `empresa`
  ADD PRIMARY KEY (`id_empresa`);

--
-- Indices de la tabla `inventario`
--
ALTER TABLE `inventario`
  ADD PRIMARY KEY (`id_inventario`),
  ADD KEY `id_empresa` (`id_empresa`);

--
-- Indices de la tabla `inventario_producto`
--
ALTER TABLE `inventario_producto`
  ADD PRIMARY KEY (`id_inventario_producto`),
  ADD KEY `id_inventario` (`id_inventario`),
  ADD KEY `id_producto` (`id_producto`);

--
-- Indices de la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`id_pedido`);

--
-- Indices de la tabla `pedido_producto`
--
ALTER TABLE `pedido_producto`
  ADD PRIMARY KEY (`id_pedido_producto`),
  ADD KEY `id_pedido` (`id_pedido`),
  ADD KEY `id_producto` (`id_producto`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id_producto`),
  ADD KEY `id_codigoqr` (`id_codigoqr`);

--
-- Indices de la tabla `producto_proveedor`
--
ALTER TABLE `producto_proveedor`
  ADD PRIMARY KEY (`id_producto_proveedor`),
  ADD KEY `id_producto` (`id_producto`),
  ADD KEY `id_proveedor` (`id_proveedor`);

--
-- Indices de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`id_proveedor`),
  ADD UNIQUE KEY `cif` (`cif`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `codigo_qr`
--
ALTER TABLE `codigo_qr`
  MODIFY `id_codigoqr` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- AUTO_INCREMENT de la tabla `empresa`
--
ALTER TABLE `empresa`
  MODIFY `id_empresa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `inventario`
--
ALTER TABLE `inventario`
  MODIFY `id_inventario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `inventario_producto`
--
ALTER TABLE `inventario_producto`
  MODIFY `id_inventario_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `pedido`
--
ALTER TABLE `pedido`
  MODIFY `id_pedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT de la tabla `pedido_producto`
--
ALTER TABLE `pedido_producto`
  MODIFY `id_pedido_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=87;

--
-- AUTO_INCREMENT de la tabla `producto_proveedor`
--
ALTER TABLE `producto_proveedor`
  MODIFY `id_producto_proveedor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  MODIFY `id_proveedor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `inventario`
--
ALTER TABLE `inventario`
  ADD CONSTRAINT `inventario_ibfk_1` FOREIGN KEY (`id_empresa`) REFERENCES `empresa` (`id_empresa`);

--
-- Filtros para la tabla `inventario_producto`
--
ALTER TABLE `inventario_producto`
  ADD CONSTRAINT `inventario_producto_ibfk_1` FOREIGN KEY (`id_inventario`) REFERENCES `inventario` (`id_inventario`),
  ADD CONSTRAINT `inventario_producto_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`);

--
-- Filtros para la tabla `pedido_producto`
--
ALTER TABLE `pedido_producto`
  ADD CONSTRAINT `pedido_producto_ibfk_1` FOREIGN KEY (`id_pedido`) REFERENCES `pedido` (`id_pedido`),
  ADD CONSTRAINT `pedido_producto_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`);

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`id_codigoqr`) REFERENCES `codigo_qr` (`id_codigoqr`);

--
-- Filtros para la tabla `producto_proveedor`
--
ALTER TABLE `producto_proveedor`
  ADD CONSTRAINT `producto_proveedor_ibfk_1` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`),
  ADD CONSTRAINT `producto_proveedor_ibfk_2` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedor` (`id_proveedor`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
