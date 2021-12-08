
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dragonballtorneo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `luchadores_dbz`
--
CREATE DATABASE dragonballtorneo;
USE dragonballtorneo;
CREATE TABLE `luchadores_dbz` (
  `IdLuchador` int(11) NOT NULL,
  `NombreLuchador` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `FechaNacimiento` date NOT NULL,
  `SwEstado` tinyint(1) NOT NULL,
  `DescripcionPeleador` text COLLATE utf8_spanish_ci NOT NULL,
  `KI` int(11) NOT NULL,
  `IdUniverso` smallint(6) NOT NULL,
  `habilidades` varchar(28) COLLATE utf8_spanish_ci NOT NULL,
  `salud` varchar(11) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `luchadores_dbz`
--

INSERT INTO `luchadores_dbz` (`IdLuchador`, `NombreLuchador`, `FechaNacimiento`, `SwEstado`, `DescripcionPeleador`, `KI`, `IdUniverso`, `habilidades`, `salud`) VALUES
(1, 'Goku', '2021-11-17', 1, 'Son Gokū es un personaje ficticio, protagonista de la serie de manga y anime Dragon Ball.', 9999, 7, 'Kame Hame Ha', '100000'),
(2, 'Freezer', '2021-11-12', 1, 'Puede transformarse en varias formas para esconder su poder de combate y poder darle uso en situaciones de riesgo.', 85000, 7, 'Death Ball', '90000'),
(3, 'Vegeta', '2021-11-21', 1, 'Vegeta, también conocido como Príncipe Vegeta. Es el príncipe de una raza guerrera extraterrestre conocida como los Saiyajin. Es extremadamente arrogante, orgulloso y trabajador; constantemente se refiere a su herencia y estatus real', 95000, 7, 'Garlick Gun', '90000'),
(4, 'Piccolo', '2021-11-29', 1, 'Primero se lo ve como la reencarnación del malvado Piccolo Daimaō  Sin embargo, más tarde se revela que él es un miembro de una especie humanoide extraterrestre llamada Namekuseijins, seres capaces de crear las esferas del dragón capaces de conceder deseo.', 75000, 7, 'Makosen', '65000'),
(5, 'Beerus', '2012-11-14', 1, 'Beerus es un dios destructor del universo 7. A menudo visto destruyendo planetas por capricho, los dos únicos deseos de Beerus son ser todo un gourmet, disfrutar de la comida que le gusta comer y luchar contra oponentes a quienes considera dignos', 500000, 7, 'Hakai', '500000'),
(6, 'Zeno Sama', '2021-08-17', 1, 'El Rey de Todo, también conocido como Zen Oo  y apodado por Son Goku como Todito , es el gobernante y dios absoluto de todos los universos y el máximo soberano de todo lo existente en Dragon Ball.', 999999999, 0, 'Aniquilacion Absoluta', '999999999'),
(7, 'Jiren', '2021-11-16', 1, 'Jiren es uno de los miembros de las Tropas del Orgullo, soldados justicieros provenientes del Universo 11 y que participa en el Torneo de la Fuerza.', 230000, 11, 'Power Impact', '170000'),
(8, 'Caulifla', '2021-11-13', 1, 'Es una saiyana del Planeta Sadala del Universo 6. Es una joven delincuente, líder de una pandilla, que fue reclutada por Cabba para ser miembro del Equipo del Universo 6 para participar en el Torneo de la Fuerza.', 98000, 6, 'Estallido Devastador', '90000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `universos_dbz`
--

CREATE TABLE `universos_dbz` (
  `IdUniverso` smallint(6) NOT NULL,
  `Universo` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `SwEstado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `universos_dbz`
--

INSERT INTO `universos_dbz` (`IdUniverso`, `Universo`, `SwEstado`) VALUES
(0, 'Indeterminado', 1),
(1, 'Universo 1', 1),
(2, 'Universo 2', 1),
(3, 'Universo 3', 1),
(4, 'Universo 4', 1),
(5, 'Universo 5', 1),
(6, 'Universo 6', 1),
(7, 'Universo 7', 1),
(8, 'Universo 8', 1),
(9, 'Universo 9', 1),
(10, 'Universo 10', 1),
(11, 'Universo 11', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `luchadores_dbz`
--
ALTER TABLE `luchadores_dbz`
  ADD PRIMARY KEY (`IdLuchador`),
  ADD KEY `FK_IdUniverso` (`IdUniverso`);

--
-- Indices de la tabla `universos_dbz`
--
ALTER TABLE `universos_dbz`
  ADD PRIMARY KEY (`IdUniverso`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `luchadores_dbz`
--
ALTER TABLE `luchadores_dbz`
  MODIFY `IdLuchador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `universos_dbz`
--
ALTER TABLE `universos_dbz`
  MODIFY `IdUniverso` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `luchadores_dbz`
--
ALTER TABLE `luchadores_dbz`
  ADD CONSTRAINT `FK_IdUniverso` FOREIGN KEY (`IdUniverso`) REFERENCES `universos_dbz` (`IdUniverso`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
