# Git Cheatsheet 

Эта шпаргалка содержит основные команды Git, которые помогут вам эффективно работать с репозиторием.

---

##  История коммитов

Просмотреть все коммиты:
```sh
git log
```

Вывести краткую историю коммитов (одна строка на коммит):
```sh
git log --oneline
```

Показать изменения в последнем коммите:
```sh
git show
```

Просмотреть коммиты в виде графа:
```sh
git log --graph --oneline --all
```

---

##  Работа с ветками

Создать новую ветку и переключиться на неё:
```sh
git checkout -b имя-ветки
```

Переключиться на существующую ветку:
```sh
git checkout имя-ветки
```

Просмотреть список всех локальных веток:
```sh
git branch
```

Просмотреть все ветки (локальные и удалённые):
```sh
git branch -a
```

Удалить локальную ветку:
```sh
git branch -d имя-ветки
```

Удалить удалённую ветку:
```sh
git push origin --delete имя-ветки
```

---

##  Работа с файлами

Добавить все файлы в индекс:
```sh
git add .
```

Добавить конкретный файл в индекс:
```sh
git add имя-файла
```

Просмотреть статус файлов в репозитории:
```sh
git status
```

Отменить `git add` (убрать файлы из индекса):
```sh
git reset HEAD имя-файла
```

---

## Коммиты

Создать новый коммит с сообщением:
```sh
git commit -m "feat: описание изменений"
```

Изменить последний коммит (например, исправить сообщение):
```sh
git commit --amend -m "fix: исправлен предыдущий коммит"
```

Отменить последний коммит, сохранив изменения в файлах:
```sh
git reset --soft HEAD~1
```

---

## Работа с удалёнными репозиториями

Добавить удалённый репозиторий:
```sh
git remote add origin https://github.com/USERNAME/REPOSITORY.git
```

Просмотреть список удалённых репозиториев:
```sh
git remote -v
```

Обновить информацию о ветках и коммитах на сервере:
```sh
git fetch origin
```

Загрузить изменения из удалённого репозитория:
```sh
git pull origin имя-ветки
```

Отправить изменения в удалённый репозиторий:
```sh
git push origin имя-ветки
```

---

## Откат изменений

Отменить изменения в файле (вернуть версию из последнего коммита):
```sh
git checkout -- имя-файла
```

Откатить коммит и сохранить изменения в файлах:
```sh
git reset --soft HEAD~1
```

Откатить коммит и удалить изменения:
```sh
git reset --hard HEAD~1
```

Откатить изменения в конкретном файле к предыдущему состоянию:
```sh
git checkout HEAD~1 -- имя-файла
```

---

## Теги (версии)

Создать новый тег версии:
```sh
git tag -a v1.0.0 -m "Release v1.0.0"
```

Просмотреть список всех тегов:
```sh
git tag
```

Удалить тег:
```sh
git tag -d v1.0.0
```

Опубликовать тег в удалённом репозитории:
```sh
git push origin v1.0.0
```

---

## Работа с `stash` (сохранение незакоммиченных изменений)

Сохранить текущие изменения без коммита:
```sh
git stash
```

Посмотреть список сохранённых изменений:
```sh
git stash list
```

Вернуть последние сохранённые изменения:
```sh
git stash pop
```

Удалить сохранённые изменения:
```sh
git stash drop
```

---

## Полезные команды

Создать новый пустой репозиторий:
```sh
git init
```

Очистить кэш (`.gitignore` не работает для уже закоммиченных файлов):
```sh
git rm -r --cached .
git add .
git commit -m "fix: updated .gitignore"
```

Игнорировать файлы с `.gitignore`:
```sh
echo "название_файла" >> .gitignore
```

---

**Эта шпаргалка поможет вам эффективно работать с Git!** 
