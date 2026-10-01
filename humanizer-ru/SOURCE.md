# Источник и установка

Оригинал: https://github.com/ilyautov/humanizer-ru

Навык: `skills/humanizer-ru`, версия 3.31.3.
Исходная ревизия: `1e035ad6b64c56c6e770ed28d076e2cbda3d1aed`.
Дата установки: 1 октября 2026 года.
Лицензия MIT сохранена в `LICENSE`.

Скопирована вся папка навыка, включая справочные материалы и сканер.
Из корня исходного репозитория добавлены `LICENSE` и `requirements.txt`.
В `SKILL.md` добавлены команда запуска сканера для Windows и совместная работа
с `scientific-writing`: научное письмо, затем стилистическая правка с сохранением
терминологии и нормативной пунктуации. Описание навыка сокращено и уточнено.
Исходный код сканера сохранён без изменений.

## Windows

Для сканера нужен современный Python. Создайте отдельное окружение и установите
зависимости из папки навыка:

```powershell
python -m venv "$env:USERPROFILE\.humanizer-ru"
& "$env:USERPROFILE\.humanizer-ru\Scripts\python.exe" -m pip install -r .\requirements.txt
```

Здесь `python` должен указывать на Python 3.10 или новее.
На компьютере владельца окружение и зависимости уже установлены.

Запуск из папки навыка:

```powershell
& "$env:USERPROFILE\.humanizer-ru\Scripts\python.exe" .\scripts\scan.py .\текст.txt
```

Для Codex папка `%USERPROFILE%\.codex\skills\humanizer-ru` связана
с этой папкой навыка. Изменения в личной папке навыков сразу доступны Codex.
