from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title='Список студентів')
table.add_column("ім'я", style = 'cyan')
table.add_column("курсовий проєкт", style ='magenta')

table.add_row('антон', 'чат-бот')
table.add_row('марія', 'гра на python')

console.print(table)