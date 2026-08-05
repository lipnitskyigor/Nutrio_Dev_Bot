# MealScan Bot

## Аналитика воронки

Уникальные юзеры на каждой ступени пейвол-воронки (win-back рассылка исключена):

```sql
SELECT event, COUNT(DISTINCT user_id)
FROM events
WHERE meta IS DISTINCT FROM 'winback'
GROUP BY event;
```

События идут в порядке: `limit_reached` → `paywall_shown` → `paywall_cta_clicked` → `plan_selected` → `purchase_completed`.
