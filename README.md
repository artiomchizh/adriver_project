# Автоматизация тестирования [AdRiver](https://www.adriver.ru/)

## **Содержание:**

____

* <a href="#tools">Технологии и инструменты</a>
* <a href="#cases">Тест-кейсы</a>
* <a href="#console">Установка и запуск</a>
* <a href="#cicd">Запуск в CI/CD</a>
* <a href="#allure">Allure отчет</a>
* <a href="#telegram">Уведомление в Telegram</a>
* <a href="#allure-testops">Интеграция с Allure TestOps</a>
* <a href="#jira">Интеграция с Jira</a>

----
<a id="tools"></a>

## <a name="Технологии и инструменты">**Технологии и инструменты:**</a>

<p align="center">  
<a href="https://www.jetbrains.com/idea/"><img src="images/pycharm-original.svg" width="50" height="50"  alt="PyCharm"/></a>  
<a href="https://https://web.telegram.org//"><img src="images/telegram-svgrepo-com.svg" width="50" height="50"  alt="Telegram"/></a>  
<a href="https://aerokube.com/selenoid/"><img src="images/selenium-svgrepo-com.svg" width="50" height="50"  alt="Selenoid"/></a>  
<a href="ht[images](images)tps://github.com/allure-framework/allure2"><img src="images/Allure.png" width="50" height="50"  alt="Allure"/></a> 
<a href="https://qameta.io/"><img src="images/AllureTestOps.png" width="50" height="50"  alt="Allure TestOps"/></a>   
<a href="https://www.jenkins.io/"><img src="images/jenkins-original.svg" width="50" height="50"  alt="Jenkins"/></a>  
<a href="https://selenoid.autotests.cloud/#/capabilities/"><img src="images/selenoid.png" width="50" height="50"  alt="Selenoid"/></a>  
</p>

<a id="cases"></a>

## <a name="Тест-кейсы">**Тест-кейсы:**</a>

____
| Тест | Описание | Severity |
|------|----------|----------|
| test_1 | Корректное открытие страницы | Critical |
| test_2 | Проверка кнопки "Login"| Critical |
| test_3 | Проверка поля ввода| Critical |
| test_4 | Проверка кнопки "Агенствам" | Normal |
| test_5 | Проверка видимости основных вкладок | Normal |
| test_6 | Скролл вниз и проверка кнопки "Политика конфиденциальности" | Normal |
| test_7 | Проверка интерактивных элементов страницы | Normal |
| test_8 | Проверка URL | Normal |

<a id="console"></a>

## Установка и запуск

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Запуск всех тестов
```bash
pytest
```

### Запуск конкретного теста

```bash
pytest tests/test_01.py 
```

### Просмотр Allure отчёта

```bash
allure serve allure-results
```
<a id="cicd"></a>

## Запуск в CI/CD

Тесты запускаются через **Jenkins** вручную.  
Браузер поднимается удалённо через **Selenoid** с включённой записью видео и VNC.

<a id="allure"></a>

## Allure отчёт

Каждый тест содержит следующие аттачменты:
- 📸 Скриншот
  ![Скриншот теста](images/site_scrin.jpg)
- 📄 Исходный код страницы
- 📋 Логи браузера
- 🎥 Запись видео выполнения теста
  ![Запись теста](images/video.gif)

<a id="telegram"></a>

  ## Уведомления в Telegram

После завершения запуска в Jenkins автоматически отправляется уведомление в Telegram с результатами тестов.

Уведомление содержит:
- 📊 Диаграмму с результатами
- ✅ Количество успешных тестов
- ❌ Количество упавших тестов
- ⏱ Продолжительность запуска
- 🔗 Ссылку на Allure отчёт

![Уведомление в Telegram](images/telega.jpg)

<a id="allure-testops"></a>

## Интеграция с Allure TestOps

В Allure TestOps хранится тест-план с ручными и автоматизированными тестами.  
Результаты автозапусков из Jenkins автоматически отображаются в Allure TestOps.

![Allure TestOps](images/testops.jpg)

<a id="jira"></a>

## Интеграция с Jira

Тест-кейсы и результаты запусков связаны с задачами в Jira.  
Из каждой задачи можно перейти к связанным тестам и результатам их выполнения.

![Jira](images/jira_scrin.jpg)

