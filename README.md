# Логика и технический редактор

Комплект русскоязычных скиллов для **Codex, Claude Code и OpenCode**.

| Скилл | Назначение | Версия |
|---|---|---|
| [logika](plugins/logika/skills/logika/SKILL.md) | Проверка и исправление аргументации, силлогизмы, логические ошибки и учебные задачи по Челпанову | 2.0.1 |
| [technical-style-editor](plugins/technical-style-editor/skills/technical-style-editor/SKILL.md) | Редактирование технических текстов с сохранением фактов, терминов, ограничений и статуса реализации | 0.2.0 |

У логики есть шесть справочников и [конспект 26 глав учебника](plugins/logika/skills/logika/docs/konspekt.md). У редактора — справочники по стилю и расширенной проверке, а также Python-скрипт для поиска формулировок, требующих ручного разбора.

## Быстрая установка для всех трёх клиентов

Нужны Git, Node.js и npm. Сначала можно посмотреть состав:

```bash
npx skills add snow-ghost/logic --list
```

Установить оба скилла в пользовательский профиль:

```bash
npx skills add snow-ghost/logic \
  --skill logika technical-style-editor \
  --global --agent codex claude-code opencode
```

Для одного клиента оставьте только его имя после `--agent`. Для одного скилла оставьте только его имя после `--skill`. Для установки в текущий проект уберите `--global`. Если нужны обычные копии вместо симлинков, добавьте `--copy`.

Это установка через [Skills CLI](https://github.com/vercel-labs/skills). Выберите один способ установки для каждого клиента: одновременная установка скилла папкой и плагином может создавать дубликаты.

## Плагины Codex

```bash
codex plugin marketplace add snow-ghost/logic
codex plugin add logika@logic
codex plugin add technical-style-editor@logic
```

В чате выберите скилл через `/skills` или укажите его имя:

```text
$logika проверь логику: Все кошки — млекопитающие. Кит — млекопитающее. Значит, кит — кошка.

$technical-style-editor отредактируй технический текст в файле docs/design.md.
```

См. [документацию по скиллам Codex](https://learn.chatgpt.com/docs/build-skills). Если новые скиллы не появились, начните новую сессию клиента.

## Плагины Claude Code

В терминале:

```bash
claude plugin marketplace add snow-ghost/logic
claude plugin install logika@logic
claude plugin install technical-style-editor@logic
```

Команды в чате после установки плагинов:

```text
/logika:logika исправь логику: После обновления сайта продажи выросли. Значит, обновление вызвало рост.

/logika:review Все кошки — млекопитающие. Кит — млекопитающее. Значит, кит — кошка.

/technical-style-editor:technical-style-editor Отредактируй файл docs/design.md.
```

При установке через Skills CLI или вручную команды короче: `/logika` и `/technical-style-editor`. Команда `/logika:review` входит в плагин; при установке папкой достаточно попросить «проверь логику».

См. [документацию по маркетплейсам Claude Code](https://code.claude.com/docs/en/plugin-marketplaces) и [скиллам](https://code.claude.com/docs/en/skills).

## OpenCode

Установка только для OpenCode:

```bash
npx skills add snow-ghost/logic \
  --skill logika technical-style-editor --global --agent opencode
```

В чате:

```text
Используй скилл logika. Проверь аргументацию этого текста: …

Используй скилл technical-style-editor. Отредактируй файл docs/design.md.
```

OpenCode загружает инструкции через встроенный инструмент `skill`. См. [официальную документацию](https://opencode.ai/docs/skills/).

## Ручная установка без Node.js

Клонируйте комплект и скопируйте нужные папки. Пример для Codex:

```bash
git clone https://github.com/snow-ghost/logic.git
cd logic
mkdir -p "$HOME/.agents/skills"
cp -R plugins/logika/skills/logika "$HOME/.agents/skills/"
cp -R plugins/technical-style-editor/skills/technical-style-editor "$HOME/.agents/skills/"
```

Для других клиентов замените каталог назначения:

| Клиент | Для пользователя | Только для проекта |
|---|---|---|
| Codex | `~/.agents/skills/` | `.agents/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| OpenCode | `~/.config/opencode/skills/` | `.opencode/skills/` |

Сохраняйте имена каталогов `logika` и `technical-style-editor` и копируйте все их вложенные файлы. Если скилл уже установлен, сохраните свои изменения перед заменой. OpenCode также читает `~/.agents/skills/` и `~/.claude/skills/`: для него не требуется отдельная копия, если скиллы уже находятся там.

Чтобы обновить ручную установку, выполните `git pull --ff-only` в клоне этого репозитория и снова скопируйте папки скиллов. Установки через Skills CLI обновляются командой `npx skills update`.

## Работа со скиллами

**Логика:** «проверь логику» запускает диагностику без переписывания текста; «исправь логику» — диагностику и правку; учебная задача — пошаговый разбор. JSON используется для явно заданных BQA/MCQA-бенчмарков. Скилл различает корректность вывода и истинность посылок.

**Технический редактор:** базовый режим исправляет стиль и структуру. Расширенный режим проверяет основания сравнений, причинных утверждений, оценок качества и готовности решения. Факты, числа, термины и статус реализации сохраняются.

Скиллы можно применить последовательно:

```text
Сначала используй logika и проверь аргументацию текста. Затем используй technical-style-editor и исправь стиль, сохранив факты и учтя найденные логические ошибки.
```

### Проверка технического стиля из терминала

Для диагностического скрипта нужен Python 3.9 или новее; внешних Python-зависимостей нет. Запуск из корня клона:

```bash
python3 plugins/technical-style-editor/skills/technical-style-editor/scripts/lint_technical_style.py \
  path/to/document.md --extended
```

Параметр `--json` включает JSON-вывод, `-` вместо пути читает стандартный ввод. Скрипт не меняет текст. Код завершения: `0` — срабатываний нет, `1` — есть места для ручной проверки, `2` — ошибка чтения. Параметры `--forbid-yo` и `--forbid-long-dash` включают соответствующие ограничения только по запросу автора.

## Структура и проверка

```text
.agents/plugins/marketplace.json      # каталог Codex
.claude-plugin/marketplace.json       # каталог Claude Code
plugins/<имя>/
  .codex-plugin/plugin.json
  .claude-plugin/plugin.json
  skills/<имя>/SKILL.md               # одни инструкции для всех клиентов
```

Проверка упаковки:

```bash
python3 -m unittest discover -s tests -v
claude plugin validate .
claude plugin validate plugins/logika
claude plugin validate plugins/technical-style-editor
```

## Источники и лицензии

Весь комплект, включая оба скилла, распространяется по [лицензии MIT](LICENSE).

Логика основана на скилле [EvilFreelancer/logika](https://github.com/EvilFreelancer/logika) версии 2.0.0, автор Pavel Rykov. Исходная лицензия MIT и уведомление об авторстве сохранены [в плагине](plugins/logika/LICENSE) и в устанавливаемой папке скилла.

Автор технического редактора — Sergei Uskov ([snow-ghost](https://github.com/snow-ghost)). Его [лицензия MIT](plugins/technical-style-editor/LICENSE) включена в плагин и в устанавливаемую папку скилла.

Подробности состава и адаптаций — в [SOURCES.md](SOURCES.md).
