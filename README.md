Тестовое задание:

1)Автоматизация: Используя любой КРОССПЛАТФОРМЕННЫЙ инструмент автоматизации тестирования, написать автоматические тесты на любом предпочитаемом языке программирования. Будет плюсом если при написании тестов будет использоваться Page Object Pattern. Результатом этого задания должны быть тестовые скрипты и краткая инструкция по их запуску.

2)Ручное тестирование: Если будут выявлены баги, написать для каждого багрепорт, провести анализ их природы.

Выполнение:

Инструкция по запуску тестов.
1)	Чтобы провести тесты нужно установить: Pycharm; Python; Appium; Appium Inspector; Android Studio 
2)	Создаем эмулятор в Android Studio и запускаем его. Проверить можно введением команды adb devices
3)	Заходим в Appium и запускаем сервер. Порт можно оставить без изменений, а хост лучше поменять на 127.0.0.1
4)	Для того, чтобы понять какие id использовать в коде запускаем Appium Inspector и прописываем Сapabilities : platformName; platformVersion; deviceName; automationName; app. После старта сессии у нас появится возможность смотреть id необходимых нам полей и кнопок.  
5)	Создаем проект в Pycharm.  По необходимости устанавливаем библиотеки. Понадобится Selenium, Appium-Python-Client, Behave. В проекте создаем папку и копируем туда тестируемое приложение. 
6)	Вставляем код и проводим необходимые тесты. 
 

  C баг-репортами можно ознакомиться по ссылке: https://docs.google.com/spreadsheets/d/1NiXLGj-S2Hy7uktdlg8mYbd2W_VLoIqE00fz4rhO4S4/edit?usp=sharing

