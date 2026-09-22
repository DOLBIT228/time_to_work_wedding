# SLA Dashboard

Робочий час налаштовується через змінні середовища або Streamlit secrets:

```toml
WORK_START = "11:00"
WORK_END = "19:00"
LUNCH_START = "14:00"
LUNCH_END = "15:00"
```

Також підтримується запис лише години, наприклад `WORK_START = 11`. Змінні
середовища мають пріоритет над однойменними значеннями в Streamlit secrets.
