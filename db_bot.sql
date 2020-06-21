-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Июн 21 2020 г., 02:49
-- Версия сервера: 5.7.24
-- Версия PHP: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `db_bot`
--

-- --------------------------------------------------------

--
-- Структура таблицы `categories`
--

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `categories`
--

INSERT INTO `categories` (`id`, `name`) VALUES
(1, 'Овощи'),
(2, 'Фрукты'),
(3, 'Мясо'),
(4, 'Рыба'),
(5, 'Хлебобулочные изделия'),
(6, 'Детское питание'),
(7, 'Крупы'),
(8, 'Макаронные изделия');

-- --------------------------------------------------------

--
-- Структура таблицы `groups`
--

CREATE TABLE `groups` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `group_name` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `groups`
--

INSERT INTO `groups` (`id`, `id_user`, `group_name`) VALUES
(1, 19471248, ' https://vk.com/murmewmur'),
(2, 19471248, ' https://vk.com/public196448452'),
(6, 19471248, ' https://vk.com/murmewmur');

-- --------------------------------------------------------

--
-- Структура таблицы `posts`
--

CREATE TABLE `posts` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `link` varchar(1000) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `posts`
--

INSERT INTO `posts` (`id`, `id_user`, `link`, `status`) VALUES
(1, 19471248, 'some_link_1', 1),
(2, 19471248, 'some_link_2', 1),
(3, 19471248, 'some_link_3', 1);

-- --------------------------------------------------------

--
-- Структура таблицы `subcategories`
--

CREATE TABLE `subcategories` (
  `id_category` int(11) NOT NULL,
  `name` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `subcategories`
--

INSERT INTO `subcategories` (`id_category`, `name`) VALUES
(7, 'Крупа~Рис~Греча~Гречка~Пшено~Ячка~Горох~'),
(8, 'Макароны~Лапша~Спагетти~Паста~'),
(1, 'Помидор~Огурец~Редис~Репа~Лук~Свекла~Морковь~Капуста~Кабачок~Сельдерей~Дайкон~Редька~Картофель~Патиссон~Баклажан~'),
(2, 'Яблоко~Персик~Груша~Абрикос~Киви~Апельсин~Мандарин~Ананас~Слива~Папайя~Маракуйя~'),
(3, 'Говядина~Свинина~Курица~Кролик~Гусь~Утка~Баранина~Фарш~Конина~Субпродукты~Супнабор~'),
(6, 'Пюре~'),
(4, 'Сельдь~Лосось~Скумбрия~Кета~Горбуша~Кальмар~Мидии~Гребешок~Путассу~Телапия~'),
(5, 'Хлеб~Батон~Булка~Булочка~Рогалик~Круассан~Ватрушка~');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `id_category` int(11) NOT NULL,
  `location` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `id_user`, `id_category`, `location`) VALUES
(1, 19471248, 1, 'ВДНХ'),
(2, 3285241, 2, 'Чертаново');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `groups`
--
ALTER TABLE `groups`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_id_category` (`id_category`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT для таблицы `groups`
--
ALTER TABLE `groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблицы `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `fk_id_category` FOREIGN KEY (`id_category`) REFERENCES `categories` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
