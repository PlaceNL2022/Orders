# Orders

Deze repo bevat de pixels die door de bot geplaatst moeten worden. Pixels die het eerst in de lijst staan worden als eerste geprobeerd. Bij aanvallen dus **vooraan** de lijst zetten.

## Format

`orders.json` gebruikt een vrij simpel format. Het is een array, die bestaat uit arrays met drie items.

- 0: de x-coordinaat van de pixel
- 1: de y-coordinaat van de pixel
- 2: de kleur van de pixel, zie mapping hieronder

`[x, y, kleur],`

Voorbeeld:

```
[0, 0, 2],
[0, 1, 31],
[0, 2, 12]
```

Kleuren-mapping:

![colors.png](kleuren-mapping)
