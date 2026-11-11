import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_parquet('titanic.parquet')
print("Файл прочитан. Строк:", len(df))
df.to_csv('titanic.csv', index=False, encoding='utf-8')
print("Сохранено в файл titanic.csv")
df2 = pd.read_csv('titanic.csv')
print("CSV прочитан. Строк:", len(df2))
print("Колонки:", list(df2.columns))
vyzhivaemost = df2.groupby('Pclass')['Survived'].mean()
print("\nДоля выживших по классам:")
print(vyzhivaemost)
plt.figure(figsize=(10, 6))
plt.bar(vyzhivaemost.index.astype(str), vyzhivaemost.values, color='steelblue')
plt.title('Выживаемость пассажиров Титаника по классу билета')
plt.xlabel('Класс билета (Pclass)')
plt.ylabel('Доля выживших')
plt.ylim(0, 1)  
plt.show()
quit()